from requests import get
from flask import Flask, request
from flask_cors import CORS
import json
import base64
app=Flask(__name__)
CORS(app)
@app.route("/")
def f():
	def OR(p, x):
		return json.loads(request.args.get(p) if request.args.get(p) is not None else x)
	headers=OR("headers", '{"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}')
	timeout=OR("timeout", "1")
	verify=OR("verify", "true")
	allow_redirects=OR("allow_redirects", "true")
	cookies=OR("cookies", "{}")
	url=request.args.get("url")
	if not url:
		return "Missing url", 400
	res=get(url, headers=headers, timeout=timeout, verify=verify, allow_redirects=allow_redirects, cookies=cookies)
	return json.dumps({
	"status": res.status_code,
	"text": res.text,
	"bytes": base64.b64encode(res.content).decode("ascii"),
	"apparent_encoding": res.apparent_encoding,
	"cookies": res.cookies.get_dict(),
	"ok": res.ok,
	"reason": res.reason,
	"time": res.elapsed.total_seconds()
	}, ensure_ascii=False)