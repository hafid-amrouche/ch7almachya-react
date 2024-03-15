"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[428],{5677:(e,s,a)=>{a.d(s,{Z:()=>t});a(2791);var l=a(184);const t=e=>{let{addTop:s=!1}=e;return(0,l.jsx)("div",{className:"col-12 col-md-6 col-xl-4 p-2",style:{minWidth:300},children:(0,l.jsxs)("div",{className:"card p-2",children:[s&&(0,l.jsxs)(l.Fragment,{children:[(0,l.jsx)("div",{className:"p-3 m-1"}),(0,l.jsx)("hr",{})]}),(0,l.jsxs)("div",{className:"d-flex flex-row  gap-2",children:[(0,l.jsx)("img",{className:"border rounded bg-color-grey",width:100,height:100}),(0,l.jsxs)("div",{className:"d-flex flex-column flex-grow-1 px-2 gap-1",children:[(0,l.jsx)("img",{className:"border rounded bg-color-grey",width:"100%",height:20}),(0,l.jsx)("img",{className:"border rounded bg-color-grey",width:"90%",height:20}),(0,l.jsx)("img",{className:"border rounded bg-color-grey",width:"80%",height:20}),(0,l.jsx)("img",{className:"border rounded bg-color-grey",width:"50%",height:20}),(0,l.jsx)("img",{className:"margin-inline-start-auto border rounded bg-color-grey",width:"60%",height:20})]})]})]})})}},1428:(e,s,a)=>{a.r(s),a.d(s,{default:()=>g});var l=a(2791),t=a(5294),r=a(7315),i=a(2046),c=a(4457),d=a(1087),n=a(8255),o=a(1835),m=a(184);const x=e=>{let{article:s,link:a,className:t,deleteArticle:x}=e;const{language:h,togglePopup:u}=(0,l.useContext)(i._),{translate:f}=(0,l.useContext)(n.O);return(0,m.jsx)("div",{className:"col-12 col-md-6 col-xl-4 p-2"+t,style:{minWidth:300},children:(0,m.jsxs)("div",{className:"p-2 card",children:[(0,m.jsx)("div",{className:"d-flex flex-row-reverse",children:(0,m.jsx)("button",{onClick:()=>{(0,c.Dd)("delete-article-"+s.id,u)},className:"btn btn-outline-danger w-fit-content",children:(0,m.jsx)("i",{className:"fa-solid fa-trash fa-xl"})})}),(0,m.jsxs)("div",{id:"delete-article-"+s.id,hidden:!0,children:[(0,m.jsx)("strong",{className:"px-3",children:f("Are you sure you want to delete this article ?")}),(0,m.jsxs)("div",{className:"d-flex flex-row-reverse gap-3 m-3",children:[(0,m.jsx)("button",{onClick:()=>{(0,c.Dd)("delete-article-"+s.id,u)},className:"btn btn-outline-dark",children:f("No")}),(0,m.jsx)("button",{className:"btn btn-danger",onClick:()=>x(s.id),children:f("Yes")})]})]}),(0,m.jsx)("hr",{}),(0,m.jsxs)(d.rU,{to:a,className:"cursor-pointer d-flex flex-row gap-2",children:[(0,m.jsx)("button",{className:"p-0 square overflow-hidden border rounded my-auto",style:{width:100,height:100},children:(0,m.jsx)(r.Z,{src:s.main_image,className:"mb-0"})}),(0,m.jsxs)("div",{className:"d-flex flex-column flex-grow-1 px-2",children:[(0,m.jsxs)("strong",{className:"cut-text",children:[s.brand_name," - ",s.title]}),(0,m.jsx)("div",{className:"cut-text",children:s.price>0?(0,m.jsxs)("span",{className:"color-theme fw-bold",children:[f("Price"),": ",s.price," ",f("Mi")]}):s.offered_price>0?(0,m.jsxs)("span",{className:"text-grey fw-bold",children:[f("Offered price"),": ",s.offered_price," ",f("Mi")]}):(0,m.jsx)("span",{className:"text-danger",children:f("No price")})}),(0,m.jsxs)("div",{className:"cut-text",children:[(0,m.jsx)("i",{className:"fa-solid fa-location-dot fa-sm"})," ",(0,m.jsxs)("span",{className:"",children:[s.state_name,s.city?", "+s.city:""]})]}),(0,m.jsxs)("div",{className:"d-flex align-items-center gap-1 cut-text mt-1",children:[(0,m.jsxs)("strong",{className:"small",children:[" ",s.likes_count," "]}),(0,m.jsx)("i",{className:" fa-solid fa-thumbs-up fa-sm"}),(0,m.jsxs)("strong",{className:"small",children:[" ",s.views," "]}),(0,m.jsx)("i",{className:"fa-solid fa-eye fa-sm"})]}),(0,m.jsx)(o.Z,{className:"small color-grey margin-inline-start-auto",time:s.created_at})]})]})]})})};var h=a(5677),u=a(213),f=a(8592);const g=()=>{const[e,s]=(0,l.useState)(!0),[a,r]=(0,l.useState)(null),[c,d]=(0,l.useState)([]),[o,g]=(0,l.useState)(!1),[j,p]=(0,l.useState)(null),[N,b]=(0,l.useState)(null),[v,y]=(0,l.useState)(null),w=(0,l.useRef)([]),k=(0,l.useRef)(!1),{userData:C}=(0,l.useContext)(u.S),A=()=>{t.Z.post("/api/dashboard/get-articles/",{"seen-articles":JSON.stringify(w.current)},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+C.token}}).then((e=>{s(!1),k.current=e.data[1],d((s=>[...s,...e.data[0]]))})).catch((e=>{s(!1),r(e)}))};(0,l.useEffect)((()=>{A()}),[]);const _=e=>{y(e),g(!0),t.Z.post("/api/dashboard/delete-article/",{article_id:e},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+C.token}}).then((s=>{d((s=>s.filter((s=>s.id!==e)))),g(!1),y(null),b(s)})).catch((e=>{g(!1),p(e),y(null)}))},{translate:S}=(0,l.useContext)(n.O),{setTitle:Z,setDescription:T}=(0,l.useContext)(i._);return(0,l.useEffect)((()=>{Z(S("Articles")+" | ".concat(S("Ch7al Machya"))),T(S("description"))}),[]),(0,m.jsxs)("div",{className:"bg-white d-flex flex-column",children:[j&&(0,m.jsx)(f.v,{variant:"danger",removeAlert:()=>{p(null)},className:"m-3",children:j.response.data.detail||j.message}),N&&(0,m.jsx)(f.v,{variant:"success",removeAlert:()=>{b(null)},className:"m-3",children:N.data.detail}),(0,m.jsxs)("div",{className:"py-3 d-flex px-1 d-flex flex-wrap",children:[c&&c.map((e=>(w.current=[...w.current,e.id],(0,m.jsx)(l.Fragment,{children:(0,m.jsx)(x,{deleteArticle:_,link:e.id+"/",article:e,className:v===e.id?" blur":""})},e.id)))),e&&Array.from({length:20},((e,s)=>s)).map((e=>(0,m.jsx)(h.Z,{addTop:!0},e))),c&&0==c.length&&!1===k.current&&!1===e&&(0,m.jsx)("h4",{className:"m-auto my-4",children:S("No Articles yet")})]}),k.current&&(0,m.jsx)("button",{disabled:e,className:"border ".concat(e?"":"border-black"," rounded-circle p-3 mb-3 mx-auto aspect-ratio-1 d-flex align-items-center"),onClick:()=>{s(!0),A()},children:(0,m.jsx)("i",{className:"fa-solid fa-plus fa-2xl"})})]})}}}]);
//# sourceMappingURL=428.3dc55d64.chunk.js.map