"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[417],{3417:(e,s,a)=>{a.r(s),a.d(s,{default:()=>x});var t=a(2791),i=a(213),l=a(5294),n=a(7689),r=a(2014),o=a(2046),c=a(1087),d=a(184);const u=e=>{let{socialLink:s,iconClass:a,username:t}=e;return s&&(0,d.jsxs)("div",{className:"d-flex py-3 border-bottom align-items-center px-3 d-flex gap-2",children:[(0,d.jsx)("i",{className:"".concat(a," fa-2xl color-theme")}),(0,d.jsx)("h4",{children:"/"}),(0,d.jsx)("span",{children:(0,d.jsx)(c.rU,{target:"_blank",to:s,className:"btn btn-success px-2 mw-100 overflow-hidden",children:(0,d.jsx)("div",{className:"overflow-hidden",children:t})})})]})};var m=a(8255);const x=()=>{const{userData:e}=(0,t.useContext)(i.S),[s,a]=(0,t.useState)(!1),[c,x]=(0,t.useState)(!0),[h,f]=(0,t.useState)(null),b=(0,n.UO)().username.replace("@",""),[w,p]=(0,t.useState)(null),[k,j]=(0,t.useState)(null),[g,N]=(0,t.useState)(50),[v,C]=(0,t.useState)(!1),y=(0,t.useRef)(null);(0,t.useEffect)((()=>{l.Z.get("/api/user/get-user-about/?username="+b,{headers:{"Content-Type":"multipart/form-data",Authorization:e.id?"Bearer "+e.token:""}}).then((e=>{f(e.data),p(Number(e.data.seller_rating)),j(Number(e.data.reviews_count)),C(e.data.is_user_rated),N(e.data.user_rate),e.data.is_user_rated&&(y.current=Number(e.data.user_rate)),x(!1)})).catch((()=>{x(!1)}),[])}),[]);const{S:S}=(0,t.useContext)(o._),{translate:_}=(0,t.useContext)(m.O);return(0,d.jsx)("div",{className:"d-flex flex-wrap my-4",children:c?(0,d.jsx)(r.a,{diam:100,className:"color-theme my-5 m-auto"}):h&&(0,d.jsxs)(d.Fragment,{children:[(0,d.jsx)("div",{className:"p-2 col-12 col-md-6",children:(0,d.jsxs)("div",{className:"bg-color-white rounded overflow-hidden border px-3",children:[Object.entries(h.info_section).map((e=>{let[s,a]=e;if(a)return(0,d.jsxs)("div",{className:"d-flex py-3 border-bottom gap-2",children:[(0,d.jsx)("strong",{style:{minWidth:100},children:s}),(0,d.jsx)("span",{className:"col-8",children:a})]},s)})),(0,d.jsx)(u,{socialLink:h.socials.website?"https://"+h.socials.website:null,iconClass:"fa-solid fa-globe",username:h.socials.website}),(0,d.jsx)(u,{socialLink:h.socials.facebook?"https://www.facebook.com/"+h.socials.facebook:null,iconClass:"fa-brands fa-square-facebook",username:h.socials.facebook}),(0,d.jsx)(u,{socialLink:h.socials.instagram?"https://www.instagram.com/"+h.socials.instagram:null,iconClass:"fa-brands fa-square-instagram",username:h.socials.instagram}),(0,d.jsx)(u,{socialLink:h.socials.tiktok?"https://www.tiktok.com/"+h.socials.tiktok:null,iconClass:"fa-brands fa-tiktok",username:h.socials.tiktok}),(0,d.jsx)(u,{socialLink:h.socials.youtube?"https://www.youtube.com/"+h.socials.youtube:null,iconClass:"fa-brands fa-square-youtube",username:h.socials.youtube}),(0,d.jsx)(u,{socialLink:h.socials.twitter?"https://www.twitter.com/"+h.socials.twitter:null,iconClass:"fa-brands fa-square-x-twitter",username:h.socials.twitter}),(0,d.jsx)(u,{socialLink:h.socials.linkedin?"https://www.linkedin.com/"+h.socials.linkedin:null,iconClass:"fa-brands fa-linkedin",username:h.socials.linkedin})]})}),(0,d.jsx)("div",{className:"p-2 col-12 col-md-6 mw-900",children:(0,d.jsxs)("div",{className:"m-auto bg-color-white rounded overflow-hidden border p-3",children:[(0,d.jsxs)("div",{className:"mt-3",children:[(0,d.jsxs)("div",{style:{fontSize:30},children:[_("Reviews")," (",k,")"]}),(0,d.jsx)("div",{className:"text-center",style:{fontSize:80},children:null!=w?w.toFixed(2)+"%":"-"})]}),e.id&&(0,d.jsxs)(d.Fragment,{children:[(0,d.jsx)("hr",{}),(0,d.jsx)("h5",{className:"mt-3",children:_(v?"You rating is":"Rate seller")}),(0,d.jsxs)("div",{className:" d-flex gap-2 align-items-center flex-wrap mt-3",children:[(0,d.jsxs)("h5",{style:{width:50},className:"d-inline text-center",children:[g," %"]}),(0,d.jsx)("input",{type:"range",step:10,min:0,max:100,onChange:e=>N(e.target.value),value:g,maxLength:3,className:"text-center border outline-0 flex-grow-1"}),(0,d.jsxs)("button",{disabled:y.current==g,className:"d-flex gap-2 btn btn-outline-success ",onClick:()=>{a(!0),l.Z.post("/api/user/add-review/",{rating:g,username:b},{headers:{"Content-Type":"multipart/form-data",Authorization:e.id?"Bearer "+e.token:""}}).then((e=>{const s=Number(e.data.rating);v?p((e=>(e+=(s-y.current)/k,y.current=Number(s),e))):(p((e=>(e=(e*k+s)/(k+1),y.current=Number(s),e))),j((e=>e+1))),N(s),C(!0),a(!1)})).catch((e=>{a(!1)}))},children:[_(v?"Update Rating":"Rate")," ",s&&(0,d.jsx)(r.a,{diam:25})]})]})]})]})})]})})}}}]);
//# sourceMappingURL=417.a89e27a5.chunk.js.map