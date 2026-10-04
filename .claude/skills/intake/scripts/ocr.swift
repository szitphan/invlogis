// OCR ảnh bằng Vision của macOS (có tiếng Việt). Dùng: swift ocr.swift <ảnh> [<ảnh>...]
// In ra từng ảnh: "=== <path>" rồi các dòng chữ theo thứ tự đọc (trên→dưới, trái→phải).
import Foundation
import Vision
import AppKit

for path in CommandLine.arguments.dropFirst() {
    print("=== \(path)")
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        print("!! không mở được ảnh"); continue
    }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["vi-VT", "en-US"]
    req.usesLanguageCorrection = true
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    let obs = (req.results ?? []).compactMap { o -> (CGRect, String)? in
        guard let t = o.topCandidates(1).first else { return nil }
        return (o.boundingBox, t.string)
    }
    // gom thành dòng: cùng hàng nếu tâm y gần nhau
    let sorted = obs.sorted { $0.0.midY > $1.0.midY }
    var lines: [[(CGRect, String)]] = []
    for o in sorted {
        if var last = lines.last, let ref = last.first, abs(ref.0.midY - o.0.midY) < ref.0.height * 0.5 {
            last.append(o); lines[lines.count - 1] = last
        } else { lines.append([o]) }
    }
    for l in lines {
        print(l.sorted { $0.0.minX < $1.0.minX }.map { $0.1 }.joined(separator: "  "))
    }
}
