"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[66],{6654:(e,t,a)=>{a.d(t,{Z:()=>n});a(2791);var s=a(184);const n=e=>{let{rows:t,value:a,...n}=e;return(0,s.jsx)("textarea",{rows:(()=>{const e=(a.match(/\n/g)||[]).length+1,s=t;return Math.min(Math.max(e,s),6)})(),style:{resize:"none"},value:a,...n})}},5066:(e,t,a)=>{a.r(t),a.d(t,{default:()=>x});var s=a(2791),n=a(213),c=a(5294),l=a(6654),i=a(8592),r=a(2014),o=a(8255),d=a(184);const x=()=>{const{userData:e,setUserData:t}=(0,s.useContext)(n.S),a={headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer ".concat(e.token)}},[x,u]=(0,s.useState)(!1),[m,h]=(0,s.useState)(!1),[p,g]=(0,s.useState)(e.extention.bio),[f,j]=(0,s.useState)(e.extention.email_public),[v,b]=(0,s.useState)(e.extention.is_page),N=(0,s.useRef)(!1);N.current=p.trim()==e.extention.bio&&v==e.extention.is_page&&f==e.extention.email_public;const{translate:k}=(0,s.useContext)(o.O);return(0,d.jsx)("div",{className:"p-2",children:(0,d.jsxs)("div",{className:"card d-flex flex-column p-3",children:[(0,d.jsxs)("div",{className:"row",children:[(0,d.jsx)("h4",{className:"color-theme",children:k("Account information")}),(0,d.jsxs)("div",{className:"about text-center p-3",children:[(0,d.jsx)("h5",{className:"p-1",children:k("Bio")}),(0,d.jsx)(l.Z,{className:"form-control text-center",onChange:e=>g(e.target.value),value:p,rows:2,maxLength:255})]}),(0,d.jsx)("div",{className:"d-flex flex-wrap",children:(0,d.jsxs)("div",{className:"align-items-center gap-3 d-flex col-12 col-sm-6 p-3",children:[(0,d.jsx)("p",{className:"mb-0",children:k("Page account")})," ",(0,d.jsx)("input",{type:"checkBox",checked:v,onChange:e=>{b(e.target.checked)}})]})}),e.extention.email_verified&&(0,d.jsx)(d.Fragment,{children:(0,d.jsx)("div",{className:"d-flex flex-wrap justify-content-center",children:(0,d.jsxs)("div",{className:"align-items-center gap-3 d-flex col-12 p-3",children:[k("Let people see your email"),(0,d.jsx)("input",{type:"checkBox",checked:f,onChange:e=>{j(e.target.checked)}})]})})})]}),m&&(0,d.jsx)(i.v,{removeAlert:()=>h(null),variant:"danger",className:"mt-3",children:m.response.data.detail||m.message}),(0,d.jsx)("div",{children:(0,d.jsx)("div",{children:(0,d.jsx)("div",{className:"d-flex flex-row-reverse",children:(0,d.jsxs)("button",{type:"button",id:"submit",name:"submit",className:"btn btn-success m-2 d-flex gap-2",onClick:async s=>{s.preventDefault(),u(!0);try{const{data:s}=await c.Z.post("/api/settings/update-account/",{bio:p.trim(),email_public:f,is_page:v},a),n={...e,profile:s.profile,page:s.page,extention:{...e.extention,...s.extention}};console.log(s),t(n),localStorage.setItem("userData",JSON.stringify(n)),u(!1),h(null)}catch(m){u(!1),h(m),console.log(m)}},disabled:N.current||m||x,children:[(0,d.jsx)("span",{children:k("Update info")}),x?(0,d.jsx)(r.a,{diam:23}):""]})})})})]})})}}}]);
//# sourceMappingURL=66.ab0dcfc9.chunk.js.map