"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[79],{79:(e,t,a)=>{a.r(t),a.d(t,{default:()=>u});var s=a(2791),l=a(8592),c=a(2046),o=a(5294),n=a(2014),r=a(213),i=a(8255),d=a(184);const u=()=>{const{userData:e,setUserData:t}=(0,s.useContext)(r.S),{browserData:a}=(0,s.useContext)(c._),[u,m]=(0,s.useState)(e.location.address),[h,p]=(0,s.useState)(e.location.city),[x,j]=(0,s.useState)(e.location.state.code),[v,g]=(0,s.useState)(e.location.location_public),f={headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer ".concat(e.token)}},[N,b]=(0,s.useState)(!1),[y,C]=(0,s.useState)(!1),S=(0,s.useRef)(!1);S.current=u.trim()==e.location.address&&h.trim()==e.location.city&&x==e.location.state.code&&v==e.location.location_public;const{translate:k}=(0,s.useContext)(i.O);return(0,d.jsx)("div",{className:"p-2 w-100",children:(0,d.jsxs)("div",{className:"card d-flex flex-column p-3",children:[(0,d.jsx)("h4",{className:"color-theme",children:"Location"}),(0,d.jsx)("div",{className:"col-sm-6 col-12",children:(0,d.jsxs)("div",{className:"form-group",children:[(0,d.jsx)("label",{children:k("State")}),(0,d.jsx)("select",{className:"form-select",onChange:e=>j(e.target.value),value:x,children:a.states.map((e=>(0,d.jsxs)("option",{value:e.code,children:[e.code," ",e.name.toUpperCase()]},e.code)))})]})}),(0,d.jsx)("div",{className:"col-sm-6 col-12",children:(0,d.jsxs)("div",{className:"form-group",children:[(0,d.jsx)("label",{htmlFor:"city",children:k("City")}),(0,d.jsx)("input",{type:"text",className:"form-control",placeholder:k("Enter city"),maxLength:50,onChange:e=>p(e.target.value),value:h})]})}),(0,d.jsx)("div",{className:"col-sm-6 col-12",children:(0,d.jsxs)("div",{className:"form-group",children:[(0,d.jsx)("label",{htmlFor:"city",children:k("Address")}),(0,d.jsx)("input",{type:"text",className:"form-control",placeholder:k("Enter address"),maxLength:50,onChange:e=>m(e.target.value),value:u})]})}),(0,d.jsx)("div",{children:(0,d.jsxs)("div",{className:"form-group align-items-center gap-3 d-flex p-3",children:[k("Let people see your location"),(0,d.jsx)("input",{type:"checkBox",checked:v,onChange:e=>{g(e.target.checked)}})]})}),y&&(0,d.jsx)(l.v,{removeAlert:()=>C(null),variant:"danger",className:"mt-3",children:y.response.data.detail||y.message}),(0,d.jsx)("div",{children:(0,d.jsx)("div",{className:"d-flex flex-row-reverse",children:(0,d.jsxs)("button",{type:"button",id:"submit",name:"submit",className:"btn btn-success m-2 d-flex gap-2",onClick:async a=>{a.preventDefault(),b(!0);try{const{data:a}=await o.Z.post("/api/settings/update-location/",{location_public:v,city:h.trim(),state:x,address:u},f),s={...e,location:a};t(s),localStorage.setItem("userData",JSON.stringify(s)),b(!1),C(null)}catch(y){b(!1),C(y),console.log(y)}},disabled:S.current||y||N,children:[(0,d.jsx)("span",{children:"Update location"}),N?(0,d.jsx)(n.a,{diam:23}):""]})})})]})})}}}]);
//# sourceMappingURL=79.dfb81b2a.chunk.js.map