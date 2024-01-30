var K=Object.defineProperty;var P=Object.getOwnPropertySymbols;var Q=Object.prototype.hasOwnProperty,$=Object.prototype.propertyIsEnumerable;var S=(e,d,a)=>d in e?K(e,d,{enumerable:!0,configurable:!0,writable:!0,value:a}):e[d]=a,i=(e,d)=>{for(var a in d||(d={}))Q.call(d,a)&&S(e,a,d[a]);if(P)for(var a of P(d))$.call(d,a)&&S(e,a,d[a]);return e};import{a as f,m as A,bj as z,u as C,c as n,aS as h,a4 as o,bk as T,ah as x,bd as y,ao as G,aJ as U,aK as W,aL as X,bl as Y,a5 as Z,aM as ee,a6 as ae,bm as te,b as ne,a7 as de,bn as ie,aN as se,aO as le,bo as ce,bp as re,aP as ue,aQ as ve,bq as oe,ae as me,aR as be,ab as ge,br as ke,I as L,A as ye,b5 as fe,ai as Ae,bs as Ce,bt as he}from"./index-5d6b5a6a.js";const Ie=f()({name:"VCardActions",props:A(),setup(e,d){let{slots:a}=d;return z({VBtn:{variant:"text"}}),C(()=>{var t;return n("div",{class:["v-card-actions",e.class],style:e.style},[(t=a.default)==null?void 0:t.call(a)])}),{}}}),pe=h("v-card-subtitle"),Ve=h("v-card-title"),Pe=f()({name:"VCardItem",props:i(i({appendAvatar:String,appendIcon:o,prependAvatar:String,prependIcon:o,subtitle:String,title:String},A()),T()),setup(e,d){let{slots:a}=d;return C(()=>{var r;const t=!!(e.prependAvatar||e.prependIcon),m=!!(t||a.prepend),c=!!(e.appendAvatar||e.appendIcon),b=!!(c||a.append),g=!!(e.title||a.title),k=!!(e.subtitle||a.subtitle);return n("div",{class:["v-card-item",e.class],style:e.style},[m&&n("div",{key:"prepend",class:"v-card-item__prepend"},[a.prepend?n(y,{key:"prepend-defaults",disabled:!t,defaults:{VAvatar:{density:e.density,icon:e.prependIcon,image:e.prependAvatar}}},a.prepend):t&&n(x,{key:"prepend-avatar",density:e.density,icon:e.prependIcon,image:e.prependAvatar},null)]),n("div",{class:"v-card-item__content"},[g&&n(Ve,{key:"title"},{default:()=>{var s,l;return[(l=(s=a.title)==null?void 0:s.call(a))!=null?l:e.title]}}),k&&n(pe,{key:"subtitle"},{default:()=>{var s,l;return[(l=(s=a.subtitle)==null?void 0:s.call(a))!=null?l:e.subtitle]}}),(r=a.default)==null?void 0:r.call(a)]),b&&n("div",{key:"append",class:"v-card-item__append"},[a.append?n(y,{key:"append-defaults",disabled:!c,defaults:{VAvatar:{density:e.density,icon:e.appendIcon,image:e.appendAvatar}}},a.append):c&&n(x,{key:"append-avatar",density:e.density,icon:e.appendIcon,image:e.appendAvatar},null)])])}),{}}}),Se=h("v-card-text"),Te=f()({name:"VCard",directives:{Ripple:G},props:i(i(i(i(i(i(i(i(i(i(i(i(i({appendAvatar:String,appendIcon:o,disabled:Boolean,flat:Boolean,hover:Boolean,image:String,link:{type:Boolean,default:void 0},prependAvatar:String,prependIcon:o,ripple:{type:Boolean,default:!0},subtitle:String,text:String,title:String},U()),A()),T()),W()),X()),Y()),Z()),ee()),ae()),te()),ne()),de()),ie({variant:"elevated"})),setup(e,d){let{attrs:a,slots:t}=d;const{themeClasses:m}=se(e),{borderClasses:c}=le(e),{colorClasses:b,colorStyles:g,variantClasses:k}=ce(e),{densityClasses:r}=re(e),{dimensionStyles:s}=ue(e),{elevationClasses:l}=ve(e),{loaderClasses:B}=oe(e),{locationStyles:D}=me(e),{positionClasses:_}=be(e),{roundedClasses:R}=ge(e),u=ke(e,a),M=L(()=>e.link!==!1&&u.isLink.value),v=L(()=>!e.disabled&&e.link!==!1&&(e.link||u.isClickable.value));return C(()=>{const E=M.value?"a":e.tag,N=!!(t.title||e.title),O=!!(t.subtitle||e.subtitle),j=N||O,q=!!(t.append||e.appendAvatar||e.appendIcon),w=!!(t.prepend||e.prependAvatar||e.prependIcon),F=!!(t.image||e.image),H=j||w||q,J=!!(t.text||e.text);return ye(n(E,{class:["v-card",{"v-card--disabled":e.disabled,"v-card--flat":e.flat,"v-card--hover":e.hover&&!(e.disabled||e.flat),"v-card--link":v.value},m.value,c.value,b.value,r.value,l.value,B.value,_.value,R.value,k.value,e.class],style:[g.value,s.value,D.value,e.style],href:u.href.value,onClick:v.value&&u.navigate,tabindex:e.disabled?-1:void 0},{default:()=>{var I;return[F&&n("div",{key:"image",class:"v-card__image"},[t.image?n(y,{key:"image-defaults",disabled:!e.image,defaults:{VImg:{cover:!0,src:e.image}}},t.image):n(Ae,{key:"image-img",cover:!0,src:e.image},null)]),n(Ce,{name:"v-card",active:!!e.loading,color:typeof e.loading=="boolean"?void 0:e.loading},{default:t.loader}),H&&n(Pe,{key:"item",prependAvatar:e.prependAvatar,prependIcon:e.prependIcon,title:e.title,subtitle:e.subtitle,appendAvatar:e.appendAvatar,appendIcon:e.appendIcon},{default:t.item,prepend:t.prepend,title:t.title,subtitle:t.subtitle,append:t.append}),J&&n(Se,{key:"text"},{default:()=>{var p,V;return[(V=(p=t.text)==null?void 0:p.call(t))!=null?V:e.text]}}),(I=t.default)==null?void 0:I.call(t),t.actions&&n(Ie,null,{default:t.actions}),he(v.value,"v-card")]}}),[[fe("ripple"),v.value&&e.ripple]])}),{}}});export{Te as V,Ve as a,Se as b,Ie as c,Pe as d};