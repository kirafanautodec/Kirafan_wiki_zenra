<!--
title: 戦闘ターンの説明
author: Ayaya
lang: jp
-->

# きらファンのターン
前書き：きららファンタジアの各スキル、異常状態、バフの持続ターン数を知っておくと、強敵やネタプレイなどの攻略をもっと理論的にできると思って、ここでターンの話をさせていただく。

## 二つのターン：
話がすこしややこしいが、数え方によって、ターンの定義が２つある。
### 全体戦闘ターン
全体戦闘ターン（以下、ターンという）は、戦場にいる、全ての実体（味方キャラ、敵キャラ及びスキルカード）の行動ごとに累計する数字である。

このターンは、異常状態、スキルリキャスト（CD）やキャラの入れ替えの計算に用いられる。

すべての異常状態（混乱/金縛り/腹ぺこ/弱気/眠り/不幸/沈黙/孤立）の持続ターンは１２ターンである。例えば、アルシーヴ戦で、アルシーヴに「眠り」をかけてから、全体の実体が計１２回行動したら、「眠り」が消滅する。また、「眠り」を途中でかけ直したら、また１２ターンからカウントダウンする。

スキルリキャストは、スキルを一回使ってから、再びそのスキルが使えるようになるまでのターン数である。

スキルのリキャストは、スキルレベルに関係する。具体的に、レベル1から14まで、レベル15から24まで、レベル25以上、それぞれ3つの数値がある。

例えば、スキル140320001のリキャストは、それぞれ23,20,16である。

無論、リキャストが極端に短いもの（異常付与など）はリキャストがレベルによって変化しない場合もある。

キャラの入れ替えも、計６ターンのCDがある。６ターン以内では、入れ替えができない。

### 行動ターン
行動ターン（以下、回行動もしくは行動という）は、各実体が持つターンである。wikiでは、「n 回行動」のように表記する。

	行動ターンは、「次回攻撃Up、n 回だけ攻撃を防げるシード、n 回だけ異常状態無効」以外のすべてのバフ・デバフの計算に用いられる。
  
	バフ・デバフリスト：
ATK	MAT	DEF	MDF	硬直係数（公式はSPDと表記）
属性耐性	属性係数
LUK（公式はクリティカル率と表記）	HATE係数（公式は狙われやすさと表記）

## 面白い仕様１：他人からかけられるバフ・デバフの行動ターン数が、自分からかける場合より、実際使える行動ターンが１多い。
由来：

キャラが行動する、バフ・デバフをかける場合、バフ・デバフの残行動数が初期化する。

キャラのバフ・デバフの残行動数は、キャラの行動の最後に引かれる。

バフ・デバフの残行動数が負になったら、バフ・デバフが消滅する。

#### 例：
	行動数が３のバフを考える。
  
自分からバフをかける場合、バフスキル使用の行動時、残行動数が３と初期化される。

バフスキルの行動が完了後、残行動数から１引かれて２となった。

バフが有効な状態で、行動を取る。完了後、残行動数２から１引かれて１となった。

バフが有効な状態で、行動を取る。完了後、残行動数１から１引かれて０となった。

バフが有効な状態で、行動を取る。完了後、残行動数０から１引かれて－１となった。

－１は０より小さいので、バフが消滅する。

実際、バフが有効な状態で、行動を取った回数は３である。

#### しかし、他人からかけられる場合。バフを受ける時点で、残行動数が３と初期化される。自分は行動していないので、残行動数から１引かれることはない。

バフが有効な状態で、行動を取る。完了後、残行動数３から１引かれて２となった。

バフが有効な状態で、行動を取る。完了後、残行動数２から１引かれて１となった。

バフが有効な状態で、行動を取る。完了後、残行動数１から１引かれて０となった。

バフが有効な状態で、行動を取る。完了後、残行動数０から１引かれて－１となった。

－１は０より小さいので、バフが消滅する。

実際、バフが有効な状態で、行動を取った回数は４である。

結論として、他人からかけられるバフ・デバフの行動ターン数が、自分からかける場合より、実際使える行動ターンが１多い。また、味方全体へのバフは、自分のみ、実際に使えるバフの行動数だけ、他のキャラより１小さい。
追記：

「きららスキル」は、実行者が「きらら」なので、すべてのキャラの使えるバフの行動数が＋１される。

戦士のオーブ１、味方全体ATK中アップ25%はソースで１回だが、実際２回使える。

戦士のオーブ２、味方単体ATK大アップ60%は、実際２回使える。

魔法のオーブ２、味方全体MAT大アップ35%は、実際２回使える。

騎士のオーブ２、味方単体DEF/MDF大アップ50% + HATE中アップ(40%)は、実際３回使える。

他のバフ系のきららスキルは、行動数がソースで３なので、実際４回使える。

## 面白い仕様２：とっておきは、タイムラインの最前のキャラの行動ターンが引かれる。
例をもって説明する。

図のように、とっておきゲージが２以上の状態で、「ゆの」の後ろにいる「かおす」だけでとっておきを使用した場合：

まず、「かおす」のとっておきの効果で、回復がはたらく。

次に、僧侶二名とも、腹ぺこがかかっているので、腹ぺこの -5%HP の判定が来るはずだが、

とっておきを発動した「かおす」ではなく、タイムラインの最前にいる「ゆの」が腹ぺこ判定された。

また、複数のキャラで一気にとっておきを発動するときは、タイムラインの最前のキャラのバフ行動数だけ１ひかれる。

## Credit：
先行研究：HydroH、紅葉、林檎アメ（敬称略）

映像提供：小小ら	文章作成：AYAYA
