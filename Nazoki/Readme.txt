class Nazokiの使い方
tree=Nazoki(要素数)で宣言できます
各オペレーションは
最大値　　tree.max
最小値　　tree.min
有無　　　tree.member(x)
追加　　　tree.insert(x)
削除　　　tree.delete(x)
次の要素　tree.successor(x)
前の要素　tree.predecessor(x)
でできます。
追加として
全要素の状態を表示する
tree.check()
と
全要素を追加する
tree.fill()
を追加しました
ともにO(u log log u)です。
また　xrangeなどを使ってるためpython3系ではうごかないです。
