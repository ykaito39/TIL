# 勉強メモ  
* background-imageをCSSで指定するときは、background-sizeでcoverを指定するといい感じに表示される。  
* 縦書きする場合はwriting-mode: vertical-rl。  
* 画面いっぱいに要素を配置する場合はheightとwidthで100vh, 100vwを指定するといい。  
* Flex-boxは要素のレイアウト方法の一つ。縦横センター配置する場合などに便利。以下のようにする。  
```css
.box{
    /* Flex box */
        display: flex;
        align-items: center; /* 縦のセンター揃え */
        justify-content: center; /* 横のセンター揃え */
        flex-direction: column; /* 子要素を縦で並べる。rowだと横並びになる */
}
```