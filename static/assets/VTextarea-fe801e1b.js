var ue=Object.defineProperty,ie=Object.defineProperties;var re=Object.getOwnPropertyDescriptors;var F=Object.getOwnPropertySymbols;var U=Object.prototype.hasOwnProperty,j=Object.prototype.propertyIsEnumerable;var E=(e,n,a)=>n in e?ue(e,n,{enumerable:!0,configurable:!0,writable:!0,value:a}):e[n]=a,h=(e,n)=>{for(var a in n||(n={}))U.call(n,a)&&E(e,a,n[a]);if(F)for(var a of F(n))j.call(n,a)&&E(e,a,n[a]);return e},R=(e,n)=>ie(e,re(n));var S=(e,n)=>{var a={};for(var l in e)U.call(e,l)&&n.indexOf(l)<0&&(a[l]=e[l]);if(e!=null&&F)for(var l of F(e))n.indexOf(l)<0&&j.call(e,l)&&(a[l]=e[l]);return a};import{a as se,b0 as ce,au as de,b1 as fe,F as ve,aw as xe,I as B,j as y,y as me,l as V,b2 as ge,u as he,ax as ye,ay as O,b3 as Ve,c as r,b4 as we,J as M,al as N,A as $,b5 as be,b6 as Fe,b7 as Ce,L as Pe,as as H,b8 as Ie,b9 as ke,ba as Re}from"./index-5d6b5a6a.js";const Ne=se()({name:"VTextarea",directives:{Intersect:ce},inheritAttrs:!1,props:h(h({autoGrow:Boolean,autofocus:Boolean,counter:[Boolean,Number,String],counterValue:Function,prefix:String,placeholder:String,persistentPlaceholder:Boolean,persistentCounter:Boolean,noResize:Boolean,rows:{type:[Number,String],default:5,validator:e=>!isNaN(parseFloat(e))},maxRows:{type:[Number,String],validator:e=>!isNaN(parseFloat(e))},suffix:String,modelModifiers:Object},de()),fe()),emits:{"click:control":e=>!0,"mousedown:control":e=>!0,"update:focused":e=>!0,"update:modelValue":e=>!0},setup(e,n){let{attrs:a,emit:l,slots:c}=n;const s=ve(e,"modelValue"),{isFocused:x,focus:J,blur:L}=xe(e),p=B(()=>typeof e.counterValue=="function"?e.counterValue(s.value):(s.value||"").toString().length),q=B(()=>{if(a.maxlength)return a.maxlength;if(!(!e.counter||typeof e.counter!="number"&&typeof e.counter!="string"))return e.counter});function K(t,u){var o,i;!e.autofocus||!t||(i=(o=u[0].target)==null?void 0:o.focus)==null||i.call(o)}const _=y(),w=y(),z=y(""),b=y(),Q=B(()=>x.value||e.persistentPlaceholder);function C(){var t;b.value!==document.activeElement&&((t=b.value)==null||t.focus()),x.value||J()}function W(t){C(),l("click:control",t)}function X(t){l("mousedown:control",t)}function Y(t){t.stopPropagation(),C(),H(()=>{s.value="",Ie(e["onClick:clear"],t)})}function Z(t){var o;const u=t.target;if(s.value=u.value,(o=e.modelModifiers)!=null&&o.trim){const i=[u.selectionStart,u.selectionEnd];H(()=>{u.selectionStart=i[0],u.selectionEnd=i[1]})}}const f=y();function v(){e.autoGrow&&H(()=>{if(!f.value||!w.value)return;const t=getComputedStyle(f.value),u=getComputedStyle(w.value.$el),o=parseFloat(t.getPropertyValue("--v-field-padding-top"))+parseFloat(t.getPropertyValue("--v-input-padding-top"))+parseFloat(t.getPropertyValue("--v-field-padding-bottom")),i=f.value.scrollHeight,P=parseFloat(t.lineHeight),I=Math.max(parseFloat(e.rows)*P+o,parseFloat(u.getPropertyValue("--v-input-control-height"))),k=parseFloat(e.maxRows)*P+o||1/0;z.value=ke(Re(i!=null?i:0,I,k))})}me(v),V(s,v),V(()=>e.rows,v),V(()=>e.maxRows,v),V(()=>e.density,v);let d;return V(f,t=>{t?(d=new ResizeObserver(v),d.observe(f.value)):d==null||d.disconnect()}),ge(()=>{d==null||d.disconnect()}),he(()=>{const t=!!(c.counter||e.counter||e.counterValue),u=!!(t||c.details),[o,i]=ye(a),[Se]=O.filterProps(e),A=Se,{modelValue:P}=A,I=S(A,["modelValue"]),[k]=Ve(e);return r(O,M({ref:_,modelValue:s.value,"onUpdate:modelValue":m=>s.value=m,class:["v-textarea v-text-field",{"v-textarea--prefixed":e.prefix,"v-textarea--suffixed":e.suffix,"v-text-field--prefixed":e.prefix,"v-text-field--suffixed":e.suffix,"v-textarea--auto-grow":e.autoGrow,"v-textarea--no-resize":e.noResize||e.autoGrow,"v-text-field--flush-details":["plain","underlined"].includes(e.variant)},e.class],style:e.style},o,I,{focused:x.value}),R(h({},c),{default:m=>{let{isDisabled:g,isDirty:T,isReadonly:ee,isValid:te}=m;return r(we,M({ref:w,style:{"--v-textarea-control-height":z.value},onClick:W,onMousedown:X,"onClick:clear":Y,"onClick:prependInner":e["onClick:prependInner"],"onClick:appendInner":e["onClick:appendInner"],role:"textbox"},k,{active:Q.value||T.value,dirty:T.value||e.dirty,disabled:g.value,focused:x.value,error:te.value===!1}),R(h({},c),{default:ae=>{let{props:le}=ae,G=le,{class:D}=G,ne=S(G,["class"]);return r(N,null,[e.prefix&&r("span",{class:"v-text-field__prefix"},[e.prefix]),$(r("textarea",M({ref:b,class:D,value:s.value,onInput:Z,autofocus:e.autofocus,readonly:ee.value,disabled:g.value,placeholder:e.placeholder,rows:e.rows,name:e.name,onFocus:C,onBlur:L},ne,i),null),[[be("intersect"),{handler:K},null,{once:!0}]]),e.autoGrow&&$(r("textarea",{class:[D,"v-textarea__sizer"],"onUpdate:modelValue":oe=>s.value=oe,ref:f,readonly:!0,"aria-hidden":"true"},null),[[Fe,s.value]]),e.suffix&&r("span",{class:"v-text-field__suffix"},[e.suffix])])}}))},details:u?m=>{var g;return r(N,null,[(g=c.details)==null?void 0:g.call(c,m),t&&r(N,null,[r("span",null,null),r(Ce,{active:e.persistentCounter||x.value,value:p.value,max:q.value},c.counter)])])}:void 0}))}),Pe({},_,w,b)}});export{Ne as V};