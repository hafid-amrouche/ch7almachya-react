"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[961],{7961:(e,a,t)=>{t.r(a),t.d(a,{default:()=>i});var s=t(2791),n=t(8255),l=t(6654),c=t(8592),r=t(5294),o=t(2014),u=t(2046),m=t(184);const i=()=>{const{translate:e}=(0,s.useContext)(n.O),[a,t]=(0,s.useState)(""),[i,h]=(0,s.useState)(!1),[d,p]=(0,s.useState)(null),[x,f]=(0,s.useState)(null),[g,v]=(0,s.useState)(""),[C,j]=(0,s.useState)(""),y=i||""==g.trim()||""==C.trim()||""==a.trim(),{setTitle:S,setDescription:b}=(0,s.useContext)(u._);return(0,s.useEffect)((()=>{S("".concat(e("Contact us")," | ").concat(e("Ch7al Machya"))),b(e("Contact our team at Ch7al machya for any information we will reply to you in less than a day"))}),[]),(0,m.jsxs)("div",{className:"container mw-500 p-0",children:[d&&(0,m.jsx)(c.v,{variant:"success",removeAlert:()=>{p(null)},children:d}),x&&(0,m.jsx)(c.v,{variant:"danger",removeAlert:()=>{f(null)},children:x.response.data.detail||x.message}),(0,m.jsxs)("form",{type:"POST",className:"card mx-2 mt-4 p-2 p-md-3 d-flex flex-column gap-3",children:[(0,m.jsx)("h4",{children:e("Contact us")}),(0,m.jsx)("input",{maxLength:100,value:g,onChange:e=>{v(e.target.value)},placeholder:e("Name"),className:"form-control"}),(0,m.jsx)("input",{type:"email",maxLength:100,value:C,onChange:e=>{j(e.target.value)},placeholder:e("Email"),className:"form-control"}),(0,m.jsx)(l.Z,{maxLength:1e3,rows:5,value:a,onChange:e=>t(e.target.value),placeholder:e("Message"),className:"form-control"}),(0,m.jsxs)("button",{disabled:y,onClick:()=>{h(!0),r.Z.post("/api/contact-us/",{name:g,email:C,message:a},{headers:{"Content-Type":"multipart/form-data"}}).then((e=>{p(e.data),h(!1),v(""),j(""),t("")})).catch((e=>{f(e),h(!1)}))},className:"btn btn-outline-success d-flex gap-2 justify-content-center",children:[e("Submit"),i&&(0,m.jsx)(o.a,{diam:"23"})]})]})]})}}}]);
//# sourceMappingURL=961.3907de39.chunk.js.map