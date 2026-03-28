.PHONY: push_deps
push_deps:
	uv run src/push_deps.py

.PHONY: push_exp
push_exp:
	uv run src/push_exp.py

.PHONY: submit
submit:
	uv run src/push_deps.py
	uv run src/push_exp.py
	uv run src/push_sub.py
