S, N = map(str, input().split())
N = int(N)
st = set()  # 集合 
for i in range(N):
    for j in range(len(S)-i):
        st.add(S[j:j+i+1])  # 文字数がi+1となるように文字列をスライスし、集合に追加する
ls = list(st)  # 集合のリスト化
print (sorted(ls)[N-1])  # ソートしてK番目の要素を取得
