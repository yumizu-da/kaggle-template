# 実験コードをkaggleに初回アップロード
.PHONY: init_exp
init_exp:
	cd exp && \
	kaggle d create -p . && \
	cd ..

# 実験コードをアップデート
.PHONY: upload_exp
upload_exp:
	cd exp && \
	kaggle d version -m 'update' -r zip && \
	cd ..

# wheelダウンロード用のnotebookをアップロード
.PHONY: upload_deps
upload_deps:
	cd deps && \
	kaggle k push && \
	cd ..

# submission notebookをアップロード
.PHONY: upload_sub
upload_sub:
	cd sub && \
	kaggle k push && \
	cd ..

# 実験結果の提出
.PHONY: submit
submit:
	make upload_exp && make upload_deps && make upload_sub
