"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[539],{5539:(e,s,a)=>{a.r(s),a.d(s,{default:()=>o});var r=a(2791),t=a(213),n=a(4457),c=a(5294),l=a(2014),u=a(8255),i=a(184);const o=()=>{const{userData:e,setUserData:s}=(0,r.useContext)(t.S),[a,o]=(0,r.useState)(e.username),d=(0,r.useRef)(),[m,h]=(0,r.useState)(!0),f=(0,r.useRef)(),[x,p]=(0,r.useState)(!1);d.current&&(m?(d.current.classList.add("success"),d.current.classList.remove("error")):(d.current.classList.add("error"),d.current.classList.remove("success")));const{translate:L}=(0,r.useContext)(u.O);return(0,i.jsx)("div",{className:"p-2 w-100",ref:d,children:(0,i.jsxs)("div",{className:"card d-flex flex-column p-3",children:[(0,i.jsxs)("div",{className:"col-12 col-sm-6 p-1",children:[(0,i.jsx)("label",{className:"form-label",children:L("Username (Latin letters only)")}),(0,i.jsx)("textarea",{placeholder:L("Username"),value:a,onChange:s=>{let a=s.target.value;(0,n.VT)(a)&&(o(a),a!=e.username&&a.length>0?c.Z.get("/api/checkUsername/?username=".concat(a)).then((e=>{e.data[0]?(h(!0),f.current.innerHTML=""):(h(!1),f.current.innerHTML=L("This username is taken"))})).catch((e=>{h(!1),f.current.innerHTML=e.response.data.detail||e.message})):(h(!0),f.current.innerHTML=""))},maxLength:50,className:"form-control search-area resize-none",rows:1}),(0,i.jsx)("label",{ref:f})]}),(0,i.jsx)("div",{className:"d-flex flex-row-reverse",children:(0,i.jsxs)("button",{disabled:!m||a==e.username||""==a,className:"btn btn-success m-2 d-flex gap-2",onClick:()=>{p(!0),c.Z.post("/api/settings/update-username/",{username:a},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+e.token}}).then((a=>{h(!0),p(!1);const r={...e,username:a.data};s(r),localStorage.setItem("userData",JSON.stringify(r))})).catch((e=>{f.current.innerHTML=e.response.data.detail,h(!1),p(!1)}))},children:[L("Update username"),x&&(0,i.jsx)(l.a,{diam:23})]})})]})})}}}]);
//# sourceMappingURL=539.cde9c74b.chunk.js.map