/* 変数とデータ型について
 * 変数:データに付けるラベル
 * データ型:
 *      文字列
 *      数値
 *      真偽値
 *      オブジェクト
 *          配列
 *          関数
 *          組み込みオブジェクト
 *      undefind    定義されていない
 *      null        ナニもない
 */

var s = "hello world",
    x   = 20,
    y   = -10;

console.log(s);//hello world
console.log(x,y);//20 -10

s += ", and you."; 
console.log(s);//hello world, and you.

s = "5" + 5;//not 10, it is "55".
console.log(s);
