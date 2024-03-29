"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[598],{676:(e,s,a)=>{a.d(s,{Z:()=>d});var t=a(2791),r=a(1087),l=a(7315),n=a(2046),c=a(8255),i=a(1835),o=a(184);const d=e=>{let{article:s,link:a,isInSavedArticles:d=!1}=e;const{language:m}=(0,t.useContext)(n._),{translate:x}=(0,t.useContext)(c.O);return(0,o.jsx)(r.rU,{to:a,className:"col-12 col-md-6 col-xl-4 p-2"+(d?" cursor-pointer":""),style:{minWidth:300},children:(0,o.jsxs)("div",{className:"card d-flex flex-row p-2 gap-2",children:[(0,o.jsx)("button",{className:"p-0 square overflow-hidden border rounded my-auto",style:{width:100,height:100},children:(0,o.jsx)(l.Z,{src:s.main_image,className:"mb-0"})}),(0,o.jsxs)("div",{className:"d-flex flex-column flex-grow-1 px-2",children:[(0,o.jsxs)("strong",{className:"cut-text",children:[s.brand_name," - ",s.title]}),(0,o.jsx)("div",{className:"cut-text",children:s.price>0?(0,o.jsxs)("span",{className:"color-theme fw-bold",children:[x("Price"),": ",s.price," ",x("Mi")]}):s.offered_price>0?(0,o.jsxs)("span",{className:"text-grey fw-bold",children:[x("Offered price"),": ",s.offered_price," ",x("Mi")]}):(0,o.jsx)("span",{className:"text-danger",children:x("No price")})}),(0,o.jsxs)("div",{className:"cut-text",children:[(0,o.jsx)("i",{className:"fa-solid fa-location-dot fa-sm"})," ",(0,o.jsxs)("span",{className:"",children:[s.state_name,s.city?", "+s.city:""]})]}),(0,o.jsxs)("div",{className:"d-flex align-items-center gap-1 cut-text mt-1",children:[(0,o.jsxs)("strong",{className:"small",children:[" ",s.likes_count," "]}),(0,o.jsx)("i",{className:" fa-solid fa-thumbs-up fa-sm"}),(0,o.jsxs)("strong",{className:"small",children:[" ",s.views," "]}),(0,o.jsx)("i",{className:"fa-solid fa-eye fa-sm"})]}),(0,o.jsx)(i.Z,{className:"small color-grey margin-inline-start-auto",time:s.created_at})]})]})})}},5677:(e,s,a)=>{a.d(s,{Z:()=>r});a(2791);var t=a(184);const r=e=>{let{addTop:s=!1}=e;return(0,t.jsx)("div",{className:"col-12 col-md-6 col-xl-4 p-2",style:{minWidth:300},children:(0,t.jsxs)("div",{className:"card p-2",children:[s&&(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)("div",{className:"p-3 m-1"}),(0,t.jsx)("hr",{})]}),(0,t.jsxs)("div",{className:"d-flex flex-row  gap-2",children:[(0,t.jsx)("img",{className:"border rounded bg-color-grey",width:100,height:100}),(0,t.jsxs)("div",{className:"d-flex flex-column flex-grow-1 px-2 gap-1",children:[(0,t.jsx)("img",{className:"border rounded bg-color-grey",width:"100%",height:20}),(0,t.jsx)("img",{className:"border rounded bg-color-grey",width:"90%",height:20}),(0,t.jsx)("img",{className:"border rounded bg-color-grey",width:"80%",height:20}),(0,t.jsx)("img",{className:"border rounded bg-color-grey",width:"50%",height:20}),(0,t.jsx)("img",{className:"margin-inline-start-auto border rounded bg-color-grey",width:"60%",height:20})]})]})]})})}},1490:(e,s,a)=>{a.d(s,{Z:()=>i});var t=a(2791),r=a(1087),l=a(2046),n=a(8255),c=a(184);const i=()=>{const{Left:e}=(0,t.useContext)(l._),{translate:s}=(0,t.useContext)(n.O);return(0,c.jsxs)("div",{className:"text-center py-5 my-5",children:[(0,c.jsx)("div",{children:(0,c.jsx)("i",{className:"fa-solid fa-triangle-exclamation text-danger",style:{fontSize:200}})}),(0,c.jsx)("h1",{className:"p-3 text-danger",children:s("Error 404")}),(0,c.jsxs)(r.rU,{to:"/",className:"w-fit-content d-flex align-items-center justify-content-center gap-3 btn btn-outline-success m-auto border-0 px-4 py-3",style:{fontSize:30},children:[(0,c.jsx)("i",{className:"fa-solid fa-arrow-".concat(e)}),s("Go back home")]})]})}},6598:(e,s,a)=>{a.r(s),a.d(s,{default:()=>_});var t=a(2791),r=a(168),l=a(7689),n=a(1087),c=a(5867),i=a(7315),o=a(5294),d=a(213),m=a(1490),x=a(8255),h=a(184);const u=e=>{let{data:s}=e;const[a,r]=(0,t.useState)(!1),{token:n}=(0,t.useContext)(d.S).userData,c=(0,l.UO)().username.replace("@",""),[i,m]=(0,t.useState)(!1);(0,t.useEffect)((()=>{s&&m(s.is_follower)}),[s]);const{translate:u}=(0,t.useContext)(x.O);return(0,h.jsxs)("button",{onClick:()=>{r(!0),o.Z.post("/api/user/profile/".concat(c,"/toggle-follower/"),{},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+n}}).then((e=>{r(!1),m(e.data)})).catch((e=>{r(!1)}))},disabled:a,className:"btn btn-success m-2",children:[s&&!i&&(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)("span",{className:"mx-1",children:u("Follow")}),(0,h.jsx)("i",{className:"fa-solid fa-user-plus"})]}),s&&i&&(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)("span",{className:"mx-1",children:u("Unfollow")}),(0,h.jsx)("i",{className:"fa-solid fa-xmark mx-1"})]}),!s&&(0,h.jsx)(h.Fragment,{children:(0,h.jsx)("div",{className:"mx-1",style:{width:80,height:24}})})]})};var p=a(4457),j=a(2046);const f=()=>{const[e,s]=(0,t.useState)(!1),{togglePopup:a,setReportData:r}=(0,t.useContext)(j._),n=(0,l.UO)().username.replace("@",""),{translate:c}=(0,t.useContext)(x.O),{Right:i}=(0,t.useContext)(j._);return(0,h.jsxs)("div",{className:"d-flex flex-row-reverse mb-2 position-relative ",children:[(0,h.jsx)("button",{className:"btn btn-outline-success m-3",onClick:()=>{(0,p.Dd)("user-profile-parameters",a),s(!1)},children:(0,h.jsx)("i",{className:"fa-solid fa-ellipsis fa-2xl"})}),(0,h.jsxs)("div",{className:"card z-index-1 parameters",id:"user-profile-parameters",hidden:!0,style:{width:250,position:"absolute",[i]:8,top:65},children:[(0,h.jsx)("div",{className:"p-3",onClick:()=>(0,p.zp)(window.location.href,s),children:e?(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)("i",{className:"fa-solid fa-check px-2 py-1 rounded mx-1"}),(0,h.jsx)("span",{className:"mx-2",children:c("Copied")})]}):(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)("i",{className:"fa-solid fa-link px-2 py-1 rounded mx-1"}),(0,h.jsx)("span",{className:"mx-2",children:c("Copy link")})]})}),(0,h.jsxs)("div",{className:"p-3",onClick:()=>{a(),r({type:"User",user_username:n})},children:[(0,h.jsx)("i",{className:"fa-solid fa-exclamation px-3 py-1 border-0 rounded mx-1"}),(0,h.jsx)("span",{className:"mx-2",children:c("Report")})]})]})]})};var g;const N=c.ZP.div(g||(g=(0,r.Z)(["\n\n.upper{\n    height: 100px;\n    background-color: #BBBBBB;\n}\n.user{\n    transform: translateY(-50%);\n    margin-bottom: -30px;\n}\n.square{\n    width: 100px;\n    margin: auto;\n}\n"]))),b=e=>{let{setError:s,setLoading:a}=e;const[r,c]=(0,t.useState)(null),m=(0,l.UO)().username.replace("@",""),{token:g,id:b}=(0,t.useContext)(d.S).userData,y=(0,t.useContext)(d.S).userData.username;let v={};v=g?{headers:{Authorization:"Bearer "+g}}:{},(0,t.useEffect)((()=>{a(!0),o.Z.get("/api/user/profile/".concat(m.toLocaleLowerCase(),"/"),v).then((e=>{c(e.data),a(!1)})).catch((e=>{s(e),a(!1)}))}),[]);const{translate:w}=(0,t.useContext)(x.O),{setTitle:C,setDescription:k}=(0,t.useContext)(j._);return(0,t.useEffect)((()=>{r&&(C("".concat(r.name.text||r.name," | ").concat(w("Ch7al Machya"))),k("".concat(r.name.text||r.name," - @").concat(r.username," ").concat(w("is on Ch7al machya"))))}),[r]),(0,h.jsx)(N,{className:"d-flex justify-content-center align-items-center",children:(0,h.jsxs)("div",{className:"col-12 bg-white",children:[(0,h.jsx)("div",{className:"upper",children:(0,h.jsx)(f,{})}),(0,h.jsx)("div",{className:"user bg-transparent",children:(0,h.jsx)("div",{className:"profile square",children:(0,h.jsx)(i.Z,{src:r&&r.image||"",className:"".concat(r?"bg-white":"bg-color-grey"," ").concat(r&&r.is_page?"":"rounded-circle"," border")})})}),(0,h.jsxs)("div",{className:"text-center center-all",children:[r?(0,h.jsxs)("h4",{className:"mb-0",children:[r.name.text||r.name," ",r.name.is_verified&&(0,h.jsx)("img",{width:"20",src:"/static/others/verified.png"})]}):(0,h.jsx)("div",{className:"bg-color-grey rounded m-auto",style:{width:200,height:30}}),r&&(0,h.jsxs)("h5",{className:"text-center fw-bold text-grey mb-3 cursor-pointer mt-1",onClick:()=>(0,p.zp)(window.location.href),children:["@",r.username,(0,h.jsx)("i",{className:"fa-regular fa-copy mx-1"})]}),r?(0,h.jsx)("p",{className:"text-muted d-block mb-0 px-2",children:r.bio}):(0,h.jsx)("div",{className:"bg-color-grey m-auto rounded mt-3",style:{width:200,height:50}}),b&&m!==y&&(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(u,{data:r}),(0,h.jsxs)(n.rU,{to:"/messages/".concat(r&&r.id,"/"),className:"btn btn-success m-2 ".concat(r?"":"color-theme"),children:[(0,h.jsx)("span",{className:"mx-1",children:w("Message")}),(0,h.jsx)("i",{className:"fa-brands fa-facebook-messenger mx-1"})]})]}),(0,h.jsxs)("div",{className:"d-flex justify-content-center gap-5 align-items-center my-3 px-4",children:[(0,h.jsxs)("div",{className:"stats",children:[(0,h.jsx)("h6",{className:"mb-0 small",children:w("Followers")}),(0,h.jsx)("span",{className:"small",children:r?r.followers_count:w("Loading...")})]}),(0,h.jsxs)("div",{className:"stats",children:[(0,h.jsx)("h6",{className:"mb-0 small",children:w("Articles")}),(0,h.jsx)("span",{className:"small",children:r?r.articles_count:w("Loading...")})]}),(0,h.jsxs)("div",{className:"stats",children:[(0,h.jsx)("h6",{className:"mb-0 small",children:w("Rank")}),(0,h.jsx)("span",{className:"small",children:r?null!==r.rank?r.rank:"-":w("Loading...")})]})]})]})]})})};var y=a(676),v=a(5677);const w=e=>{let{error:s,loading:a}=e;const[r,n]=(0,t.useState)(null),[c,i]=(0,t.useState)(!0),[d,m]=(0,t.useState)([]),u=(0,l.UO)().username.replace("@",""),p=(0,t.useRef)([]),j=(0,t.useRef)(!1),f=()=>{o.Z.post("/api/user/profile/".concat(u,"/get-articles/"),{"seen-articles":JSON.stringify(p.current)},{headers:{"Content-Type":"multipart/form-data"}}).then((e=>{i(!1),j.current=e.data[1],m((s=>[...s,...e.data[0]]))})).catch((e=>{i(!1),n(e)}))};(0,t.useEffect)((()=>{a||s||f(),!a&&s&&(j.current=!1)}),[s,a]);let g=0;const{translate:N}=(0,t.useContext)(x.O);return(0,h.jsxs)("div",{className:"d-flex flex-column",children:[(0,h.jsxs)("div",{className:"py-3 d-flex px-1 justify-content-center d-flex flex-wrap",children:[d&&d.map((e=>(g+=1,p.current=[...p.current,e.id],(0,h.jsx)(t.Fragment,{children:(0,h.jsx)(y.Z,{link:"/redirect/?redirect="+e.url,article:e})},e.id)))),d&&0==d.length&&!1===j.current&&!1===c&&(0,h.jsx)("h4",{className:"m-3",children:N("No Articles yet")}),c&&Array.from({length:20},((e,s)=>s)).map((e=>(0,h.jsx)(v.Z,{},e)))]}),j.current&&(0,h.jsx)("button",{disabled:c,className:"border ".concat(c?"":"border-black"," rounded-circle p-3 mb-3 mx-auto aspect-ratio-1 d-flex align-items-center"),onClick:()=>{i(!0),f()},children:(0,h.jsx)("i",{className:"fa-solid fa-plus fa-2xl"})})]})};var C=a(9902);const k=(0,h.jsx)(C.Z,{Component:(0,t.lazy)((()=>a.e(417).then(a.bind(a,3417))))}),_=()=>{const[e,s]=(0,t.useState)(null),[a,r]=(0,t.useState)(!0),[l,n]=(0,t.useState)(!0),c=(0,t.useRef)(!1);!l&&(c.current=!0);const{togglePopup:i}=(0,t.useContext)(j._),{translate:o}=(0,t.useContext)(x.O);return e?(0,h.jsx)(m.Z,{}):(0,h.jsxs)(h.Fragment,{children:[(0,h.jsx)(b,{setError:s,setLoading:r}),(0,h.jsxs)("div",{className:"d-flex",children:[(0,h.jsx)("button",{onClick:()=>{n(!0),i()},className:"col-6 text-center py-2 bg-color-white".concat(l?" bg-color-dark-white":""),children:o("Articles")}),(0,h.jsx)("button",{onClick:()=>{n(!1),i()},className:"col-6 text-center py-2 bg-color-white".concat(l?"":" bg-color-dark-white"),children:o("About")})]}),(0,h.jsx)("div",{hidden:!l,children:(0,h.jsx)(w,{error:e,loading:a})}),c.current&&(0,h.jsx)("div",{hidden:l,children:k})]})}}}]);
//# sourceMappingURL=598.40a2120d.chunk.js.map