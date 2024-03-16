"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[700],{1490:(e,t,n)=>{n.d(t,{Z:()=>o});var s=n(2791),a=n(1087),i=n(2046),d=n(8255),r=n(184);const o=()=>{const{Left:e}=(0,s.useContext)(i._),{translate:t}=(0,s.useContext)(d.O);return(0,r.jsxs)("div",{className:"text-center py-5 my-5",children:[(0,r.jsx)("div",{children:(0,r.jsx)("i",{className:"fa-solid fa-triangle-exclamation text-danger",style:{fontSize:200}})}),(0,r.jsx)("h1",{className:"p-3 text-danger",children:t("Error 404")}),(0,r.jsxs)(a.rU,{to:"/",className:"w-fit-content d-flex align-items-center justify-content-center gap-3 btn btn-outline-success m-auto border-0 px-4 py-3",style:{fontSize:30},children:[(0,r.jsx)("i",{className:"fa-solid fa-arrow-".concat(e)}),t("Go back home")]})]})}},6700:(e,t,n)=>{n.r(t),n.d(t,{default:()=>b});var s=n(2791),a=n(7522),i=n(9032),d=n(6654),r=n(5294),o=n(7689),c=n(1087),l=n(213),m=n(4457),u=n(2046),x=n(1835),g=n(184);const h=e=>{let{message:t,lastMessageId:n}=e;const{togglePopup:a}=(0,s.useContext)(u._),{language:i}=(0,s.useContext)(u._).browserData;return(0,g.jsxs)(g.Fragment,{children:[(0,g.jsx)(x.Z,{language:i,time:t.sent_at,hidden:!0,id:"message-time-".concat(t.id),className:"px-2 small text-grey"}),(0,g.jsx)("button",{onClick:()=>{(0,m.Dd)("message-time-".concat(t.id),a),n==t.id&&setTimeout((()=>{document.getElementById("chatbox").scrollTop=0}),0)},className:"py-2 px-3  w-fit-content m-1 btn btn-success small text-start",style:{maxWidth:"70%"},children:t.text})]})};var f=n(8255);const p=e=>{let{message:t,lastMessageId:n}=e;const{togglePopup:a,Right:i}=(0,s.useContext)(u._),{language:d}=(0,s.useContext)(u._).browserData,r=t.state||"sent",{translate:o}=(0,s.useContext)(f.O);return(0,g.jsxs)("div",{className:"".concat("ar"==d?"d-ltr":"d-rtl"),children:[(0,g.jsxs)("div",{className:"d-flex align-items-end",children:[(0,g.jsx)("span",{className:"position-relative",children:(0,g.jsx)("i",{hidden:"sent"==r,className:"".concat("notSent"===r?"fa-solid fa-triangle-exclamation text-danger":"fa-regular fa-paper-plane color-theme"," fa-xs")})}),(0,g.jsx)("button",{onClick:()=>{(0,m.Dd)("message-time-".concat(t.id),a),n==t.id&&setTimeout((()=>{document.getElementById("chatbox").scrollTop=0}),0)},className:"py-2 px-3 w-fit-content m-1 border rounded-4 ".concat("notSent"===r?"border-danger text-danger":"border-success color-theme"," small text-start"),style:{maxWidth:"70%"},children:t.text})]}),"Sending"===t.sent_at?(0,g.jsx)("span",{id:"message-time-".concat(t.id),hidden:!0,className:"px-2 small color-theme",children:o("Sending")}):"Not sent"===t.sent_at?(0,g.jsx)("span",{id:"message-time-".concat(t.id),hidden:!0,className:"px-2 small text-danger",children:o("Not sent")}):(0,g.jsx)(x.Z,{language:d,time:t.sent_at,hidden:!0,id:"message-time-".concat(t.id),className:"px-2 small text-grey"})]})};var y=n(2014),w=n(1490);new BroadcastChannel("myChannel");const j=e=>{let{conversationsWidth:t}=e,n=window.innerWidth>=750;const a=(0,s.useRef)(),{friendId:m}=(0,o.UO)(),[x,j]=(0,s.useState)(!1),[b,v]=(0,s.useState)(""),{userData:N}=(0,s.useContext)(l.S),C=(0,s.useRef)(0),[S,E]=(0,s.useState)(null),_=(0,s.useRef)(!1),[I,B]=(0,s.useState)(!0),[W,T]=(0,s.useState)(null),[k,z]=(0,s.useState)([]),D=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null;r.Z.post("/api/messaging/get-messages/",{"seen-messages":JSON.stringify(null==e?k.map((e=>e.id)):[]),"friend-id":m},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer ".concat(N.token)}}).then((e=>{e.data[2]&&E(e.data[2]),B(!1),H(!1),_.current=e.data[1],z((t=>[...t,...e.data[0]])),setTimeout((()=>{document.getElementById("chatbox").scrollTop=0}),0)})).catch((e=>{B(!1),H(!1),T(e),document.getElementById("Header").removeAttribute("hidden")}))},O=(0,o.TH)();(0,s.useEffect)((()=>{E(null),_.current=!1,B(!0),z([]),D([])}),[O]);const[Z,H]=(0,s.useState)(!1);(0,s.useEffect)((()=>{if(N.id){const e=new WebSocket("ws://127.0.0.1:8000/chat-room/?token=".concat(N.token,"&friend-id=").concat(m));return e.onmessage=e=>{const t=JSON.parse(e.data);"message-update"===t.type&&(z((e=>[t.message,...e.filter((e=>"sending"!==e.state))])),document.getElementById("chatbox").scrollTop>-66&&setTimeout((()=>{document.getElementById("chatbox").scrollTop=0}),0))},()=>{e.close()}}}),[m]);const{Left:P,S:A,E:L}=(0,s.useContext)(u._),{translate:M}=(0,s.useContext)(f.O);return W?(0,g.jsx)(w.Z,{}):(0,g.jsxs)("div",{className:"bg-white d-flex flex-column vh-100 flex-grow-1 z-index-1",children:[(0,g.jsxs)("div",{className:"fixed-top bg-white ms-conversation",style:{marginInlineStart:t,width:window.innerWidth-t,maxWidth:window.innerWidth},children:[(0,g.jsxs)("div",{className:"gap-2 d-flex align-items-center my-1 p".concat(A,"-3 cursor-pointer"),children:[!n&&(0,g.jsx)(c.rU,{to:"/messages/",className:"btn btn-outline-success border-0",children:(0,g.jsx)("i",{className:"fa-solid fa-chevron-".concat(P)})}),(0,g.jsx)(c.rU,{to:S?"/@".concat(S.friend_username,"/"):"",children:S?(0,g.jsxs)(g.Fragment,{children:[(0,g.jsx)(i.q,{src:S.friend_image}),(0,g.jsxs)("strong",{children:[S.friend_name.text||S.friend_name," ",S.friend_name.is_verified&&(0,g.jsx)("img",{width:"16",src:"/static/others/verified.png"})]})]}):(0,g.jsxs)(g.Fragment,{children:[(0,g.jsx)("img",{width:40,height:40,className:"bg-secondary rounded rounded-circle mt-1"}),(0,g.jsx)("img",{width:150,height:20,className:"bg-secondary rounded mx-2"})]})})]}),(0,g.jsx)("hr",{className:"m-0"})]}),I?(0,g.jsx)("div",{className:"d-flex align-items-center justify-content-center vh-100",children:(0,g.jsx)(y.a,{className:"color-theme",diam:"100"})}):(0,g.jsx)("div",{style:{position:"fixed",bottom:54,height:"calc(100% - 103px)",width:"calc( 100% - ".concat(t,"px)")},children:(0,g.jsxs)("div",{className:"overflow-auto d-flex flex-column-reverse flex-grow-1 fixed-middle h-100 mw-100",style:{padding:"0 8px 8px 8px"},id:"chatbox",ref:a,children:[(0,g.jsx)("div",{id:"flag"}),k.map((e=>e.sender===N.id?(0,g.jsx)(p,{lastMessageId:k[0].id,message:e},e.id):(0,g.jsx)(h,{lastMessageId:k[0].id,message:e},e.id))),_.current&&(0,g.jsx)("button",{disabled:Z,className:"".concat(Z?"":"color-theme "," text-center p-3 h4"),onClick:()=>{H(!0),D()},children:M("Show older")})]})}),(0,g.jsxs)("div",{className:"d-flex gap-1 bg-white col-12 border-top fixed-bottom px-1",style:{marginInlineStart:t,width:window.innerWidth-t,maxWidth:window.innerWidth},children:[(0,g.jsx)(d.Z,{value:b,onChange:e=>{v(e.target.value)},rows:"1",className:"flex-grow-1 h-fit-content my-1 border rounded p-2",maxLength:255,style:{resize:"none",outline:"none"}}),(0,g.jsx)("button",{disabled:x||!b.trim(),onClick:()=>{j(!0),v(""),z((e=>[{id:"toBeDeleted",text:b,sent_at:"Sending",state:"sending",sender:N.id},...e])),setTimeout((()=>{document.getElementById("chatbox").scrollTop=0}),0),r.Z.post("/api/messaging/send-message/",{friend_id:m,text:b},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer ".concat(N.token)}}).then((e=>{j(!1)})).catch((e=>{j(!1),z((e=>(C.current+=1,e=e.filter((e=>"sending"!==e.state)),[{id:"NotSent"+C.current,text:b,sent_at:"Not sent",state:"notSent",sender:N.id},...e])))}))},className:"btn btn-outline-success px-2 m".concat(L,"-1 rounded-1 my-1 border-0 my-2 h-fit-content align-self-end ").concat("left"!=P&&"fa-flip-horizontal"),children:(0,g.jsx)("i",{className:"fa-regular fa-paper-plane fa-xl"})})]})]})},b=()=>{(0,s.useEffect)((()=>(document.getElementById("Header")&&document.getElementById("Header").setAttribute("hidden",""),document.getElementById("main").style.setProperty("padding","0"),document.getElementById("main").style.setProperty("margin-top","0"),()=>{document.getElementById("Header")&&document.getElementById("Header").removeAttribute("hidden"),document.getElementById("main").style.removeProperty("padding"),document.getElementById("main").style.removeProperty("margin-top")})),[]);const[e,t]=(0,s.useState)(!1),n=(0,s.useRef)(0);let i=window.innerWidth>=750;(0,s.useEffect)((()=>{const e=()=>{window.innerWidth<750?n.current=0:window.innerWidth>1250?n.current=500:n.current=.4*window.innerWidth,t((e=>!e))};return e(),window.addEventListener("resize",e),()=>{window.removeEventListener("resize",e)}}),[]);const{conversations:d,setConversations:r}=(0,s.useContext)(l.S),{friendId:c}=(0,o.UO)(),{language:m}=(0,s.useContext)(u._).browserData,{setTitle:x,setDescription:h}=(0,s.useContext)(u._),{translate:p}=(0,s.useContext)(f.O);return(0,s.useEffect)((()=>{x(p("ChatBox")+" | ".concat(p("Ch7al Machya"))),h(p("description"))}),[]),(0,s.useEffect)((()=>{if(d){const e=d.find((e=>e.friend_id==c));e&&0==e.is_seen&&r((e=>(e.forEach((e=>(e.friend_id==c&&(e.is_seen=!0),e))),e)))}}),[d]),(0,g.jsxs)("div",{style:{marginInlineStart:n.current},className:"d-flex",children:[i&&(0,g.jsx)("div",{className:"fixed-top bg-white h-100 overflow-y-auto border-".concat("ar"==m?"start":"end"),style:{width:n.current},children:(0,g.jsx)(a.default,{fetchConversations:!1})}),(0,g.jsx)(j,{conversationsWidth:n.current})]})}}}]);
//# sourceMappingURL=700.3d62ad4c.chunk.js.map