# 実験コードをkaggleに初回アップロード
# 実験結果の提出
.PHONY: submit
submit:
	uv run src/push_deps.py
	uv run src/push_exp.py
