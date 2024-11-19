import urllib.parse

def write_password_decoded_file(encoded_file: str, decoded_file: str) -> None:
    input_file = encoded_file  # パーセントエンコードされたテキストが含まれるファイル
    output_file = decoded_file  # デコードされたテキストを保存するファイル

    try:
        # 元のファイルを読み込み
        with open(input_file, "r", encoding="utf-8") as infile:
            encoded_content = infile.read()

        # パーセントエンコーディングをデコード
        decoded_content = urllib.parse.unquote(encoded_content)

        # デコード結果を新しいファイルに書き込み
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(decoded_content)

        print(f"デコードされた内容を '{output_file}' に保存しました。")

    except FileNotFoundError:
        print(f"入力ファイル '{input_file}' が見つかりませんでした。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":

    #4つ目
    with open("decoded-app.log") as fin:
        lines = [line.strip() for line in fin.readlines()]
    for line in lines:
        try:
            print(chr(int(line.split("!=")[1].split(")")[0][5:])), end= '')
        except Exception as e:
            pass
    
