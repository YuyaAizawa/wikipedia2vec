# Wikipedia2Vec

教師無し学習で文章の特徴抽出をする試み．

1. Wikipediaで学習
2. Wikipediaの記事ごとに埋め込みを生成し，タイトルと紐づけ
3. クエリの埋め込みを生成し，ベクトル検索で類似した記事を得る

## Setup

`./docker/run.sh`の`-v ~/datasets/huggingface_datasets:$WORK_DIR/wikipedia2vec/data`にキャッシュの場所を指定

```bash
$ ./docker/build.sh
$ ./docker/run.sh
```

### 確認

```bash
$ python ./src/test.py
```
