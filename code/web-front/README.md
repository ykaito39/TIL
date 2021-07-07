# 勉強メモ  
* background-imageをCSSで指定するときは、`background-size: cover;`を指定するといい感じに表示される。  
```css
.bg{
    background-image: url(./PC250035.JPG);
    background-size: cover; /* アス比維持で最小限表示できるように */
    background-position: center;
    overflow: hidden;
}
```
* 縦書きする場合は`writing-mode: vertical-rl`。  
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

## scroll-snap  
* scroll-snapを使うときは、親要素と子要素を以下のようにする。子要素がピタッと止まるようになる。    
```css
.snap-area{
    height: 300px;
    overflow: scroll;
    scroll-snap-stop: always;
    scroll-snap-type: y mandatory;
}

.snap-box{
    height: 200px;
    scroll-snap-align: start;
}
```  
  
overflowを指定する必要があるが、スクロールバーが表示されないようにするためには以下のようにする。chromium, safariはwebkitで指定が必要。  
```css
.snap-area{
    height: 300px;
    overflow: scroll;

    /* スクロール可能にして、スクロールバーを消す */
    /* chrome, safariは::-webkit-scrollbarも必要 */
    scrollbar-width: none; 
    
    scroll-snap-stop: always;
    scroll-snap-type: y mandatory;
}

/* スクロール可能にして、スクロールバーを消す(chrome, safari) */
::-webkit-scrollbar{
    display:none;
}
```
  
## sticky  
スクロールして、特定の要素が画面の特定の場所に来たら止めたい場合。  
親要素にposition:relativeを指定し、止めたい要素にstickyを指定する。  
positionを指定するtopやbottomで、止めたい位置を指定する。  
```css
.stick{
    height: auto;
    background-color: chocolate;
    position: -webkit-sticky; /* safari */
    position: sticky; /* 要素が[topとかbottom]に当たると止まる */
    top: 0;
}
```