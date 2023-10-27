import Foundation

let url = URL(string: "https://shiftheroes.fr/api/v1/plannings/LQfrZg/shifts/OAF6DPq/reservations")!
let headers = [
    "Authorization": "Bearer 376f0a25129fda22f7fc44398757efc7"
]

var request = URLRequest(url: url)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers

let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
    if let error = error {
        print(error)
    } else if let data = data {
        let str = String(data: data, encoding: .utf8)
        print(str ?? "")
    }
}

task.resume()