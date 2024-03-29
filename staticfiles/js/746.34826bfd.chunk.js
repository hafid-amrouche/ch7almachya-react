"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[746],{9785:(e,s,a)=>{a.d(s,{Z:()=>t});a(2791);var l=a(184);const t=function(e){let{children:s,className:a}=e;return(0,l.jsx)("div",{className:"mx-auto "+a,children:(0,l.jsx)("div",{className:"bg-color-white p-md-4 p-3 px-md-3 rounded border mx-3",children:(0,l.jsx)("div",{className:"row justify-content-md-center",children:(0,l.jsx)("div",{className:"col-xs-12",children:s})})})})}},3901:(e,s,a)=>{a.d(s,{Z:()=>x});var l,t,r=a(168),n=a(2791),i=a(5867),o=a(7315),c=a(8255),d=a(184);const m=i.ZP.div(l||(l=(0,r.Z)(["\npadding-inline-start: 10px;\npadding-inline-end: 10px;\npadding-top:7px;\npadding-bottom: 7px;\nborder-radius: 4px;\ncursor: default;\n"]))),h=i.ZP.div(t||(t=(0,r.Z)(["\npadding-top: 1px;\n.option:hover:not(.disabled),\n.option:active:not(.disabled){\n    background-color: var(--theme);\n    color: var(--white);\n}\n.option{    \n    padding: 8px;\n}\n.option.disabled{\n    padding: 8px !important;\n    opacity: 0.2;\n}\n\ncursor: default;\n"]))),x=e=>{let{value:s,setValue:a,options:l,showSearch:t=!0,emptySelection:r=!1}=e;(0,n.useEffect)((()=>{a(s)}),[]);const[i,x]=(0,n.useState)(!1);let u;u=i?"M18 15 12 9 6 15":"M6 9L12 15 18 9";const p=(0,n.useRef)();(0,n.useEffect)((()=>{const e=e=>{const s=e.detail.target;p.current.contains(s)||b.current.contains(s)?p.current.contains(s)&&!j.current.contains(s)&&x((e=>!e)):x(!1)};return document.addEventListener("global-click",e),()=>{document.removeEventListener("global-click",e)}}),[]);const f=l&&l.find((e=>e&&e.value==s)),g=f?f.label:"",j=(0,n.useRef)(),b=(0,n.useRef)(),[v,N]=(0,n.useState)(""),w=l.filter((e=>e&&(!e.disabled||!v.trim())&&e.label.toLowerCase().includes(v.toLowerCase().trim()))),{translate:y}=(0,n.useContext)(c.O);return(0,d.jsxs)(d.Fragment,{children:[(0,d.jsxs)(m,{ref:p,className:"bg-color-white border d-flex justify-content-between",children:[(0,d.jsx)("div",{children:g}),(0,d.jsxs)("div",{children:[(0,d.jsxs)("svg",{hidden:!f||r,className:"cursor-pointer",ref:j,width:"24",height:"24",fill:"none",stroke:"currentColor",strokeWidth:"2",onClick:e=>{x(!1),a(-1)},children:[(0,d.jsx)("line",{x1:"18",y1:"6",x2:"6",y2:"18"}),(0,d.jsx)("line",{x1:"6",y1:"6",x2:"18",y2:"18"})]}),(0,d.jsx)("svg",{width:"24",height:"24",fill:"none",stroke:"currentColor",strokeWidth:"2",children:(0,d.jsx)("path",{d:u})})]})]}),(0,d.jsx)(h,{hidden:!i,children:(0,d.jsx)("div",{className:"position-relative",style:{margin:"0 2px"},children:(0,d.jsxs)("div",{ref:b,className:"position-absolute bg-color-white z-1 w-100 rounded-inheret border",children:[t&&l.length>1&&(0,d.jsxs)(d.Fragment,{children:[(0,d.jsxs)("div",{className:"d-flex align-items-center",children:[(0,d.jsx)("input",{placeholder:"Recharche",className:"search-area flex-grow-1 p-2",rows:1,value:v,onChange:e=>N(e.target.value)}),(0,d.jsxs)("svg",{hidden:""==v.trim(),className:"cursor-pointer mx-1",width:"24",height:"24",fill:"none",stroke:"currentColor",strokeWidth:"2",onClick:e=>{N("")},children:[(0,d.jsx)("line",{x1:"18",y1:"6",x2:"6",y2:"18"}),(0,d.jsx)("line",{x1:"6",y1:"6",x2:"18",y2:"18"})]})]}),(0,d.jsx)("hr",{className:"m-0 border-black"})]}),(0,d.jsx)("div",{style:{maxHeight:"40vh",overflowY:"auto"},children:w.map((e=>e&&(0,d.jsx)(n.Fragment,{children:(0,d.jsxs)("div",{className:"".concat(e.disabled?"disabled ":"","option d-flex gap-2 align-items-center"),onClick:()=>{e.disabled||(N(""),a(e.value),x(!1))},children:[(0,d.jsx)(o.Z,{src:e.icon,width:"30"}),(0,d.jsx)("span",{children:e.label})]})},e.value)))}),0==w.length&&(0,d.jsx)("p",{className:"text-center flex-grow-1 py-2 my-1",children:y("No option was found")})]})})})]})}},508:(e,s,a)=>{a.d(s,{Z:()=>o});var l=a(2791),t=a(2046),r=a(3901),n=a(8255),i=a(184);const o=e=>{let{brand:s,setBrand:a,category:o,emptySelection:c}=e;const{browserData:d}=(0,l.useContext)(t._),m=d.brands;let h=[];m.forEach((e=>{(-1!=o&&d.categories.find((e=>e.id==o)).brands.includes(e.id)||-1==o)&&93!=e.id&&(h=[...h,{value:e.id,icon:e.icon,label:e.name}])}));const x=d.brands.find((e=>93==e.id)),u=h.sort(((e,s)=>e.label.localeCompare(s.label)));h=[...u,{value:x.id,icon:x.icon,label:"\u0639\u0644\u0627\u0645\u0629 \u0623\u062e\u0631\u0649"}],(0,l.useEffect)((()=>{if(c){const e=d.categories.find((e=>e.id==o));if(-1!=o&&!e.brands.includes(s))if(h.length>1){const e=h.filter((e=>e&&!e.disabled))[0];a(e.value)}else a(93)}}),[o]);const{translate:p}=(0,l.useContext)(n.O);return(0,i.jsxs)("div",{className:"p-2",children:[(0,i.jsx)("label",{className:"form-label",children:(0,i.jsx)("strong",{children:p("Brand")})}),(0,i.jsx)(r.Z,{value:s,setValue:a,options:h,emptySelection:c})]})}},7664:(e,s,a)=>{a.d(s,{Z:()=>o});var l=a(2791),t=a(3901),r=a(2046),n=a(8255),i=a(184);const o=e=>{let{category:s,setCtegory:a,emptySelection:o}=e;const{browserData:c}=(0,l.useContext)(r._);let d=c.categories.sort(((e,s)=>e.order-s.order)).map((e=>({value:e.id,label:e.name,icon:e.icon})));d=[null,...d];const{translate:m}=(0,l.useContext)(n.O);return(0,i.jsxs)("div",{className:"p-2",children:[(0,i.jsx)("label",{className:"form-label",children:(0,i.jsx)("strong",{children:m("Category")})}),(0,i.jsx)(t.Z,{showSearch:!1,value:s,setValue:a,options:d,emptySelection:o})]})}},10:(e,s,a)=>{a.r(s),a.d(s,{default:()=>k});var l,t=a(2791),r=a(2046),n=a(213),i=a(8592),o=a(2014),c=a(9785),d=a(5294),m=a(4457),h=a(7689),x=a(6167),u=a(168),p=(a(8022),a(5931)),f=a.n(p),g=a(5867),j=a(8255),b=a(184);const v=g.ZP.div(l||(l=(0,u.Z)(["\npadding: 5px;\nborder: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color);\nborder-radius: 10px;\n.dzu-dropzone{\n  z-index: 0;\n  overflow: auto;\n  border: none;\n  background-color: var(--white);\n  min-height: unset;\n}\n.dzu-inputLabelWithFiles{\n  color: var(--theme);\n  background-color: var(--white);\n  border: var(--theme) 2px solid;\n  margin: 10px auto 20px auto;\n  border-radius: 50%;\n  font-size: 30px;\n}\n.dzu-inputLabelWithFiles:hover,\n.dzu-inputLabelWithFiles:active,\n.dzu-inputLabelWithFiles:focus{\n  color: var(--white);\n  background-color: var(--theme);\n}\n.dzu-inputLabel{\n  display: none;\n}\n.dzu-submitButtonContainer{\n  display: none;\n}\n.dzu-submitButton {\n  background-color: var(--theme);\n}\n.dzu-previewContainer{\n  padding: 10px;\n  margin: 10px;\n  align-items: unset;\n  width: -webkit-fill-available;\n  border: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color);;\n  border-radius: 5px;\n  display: flex;\n  min-width: unset;\n}\n.dzu-previewStatusContainer{\n  align-items: unset;\n  position: absolute;\n  top: 5px;\n  right: 5px;\n  border-radius: 4px;\n\n}\nprogress{\n  display: none;\n}\n.dzu-previewButton{\n    background-size: 25px 25px;\n    width: 25px;\n    height: 25px;\n    margin: 2px 1px 1px 2px;\n    opacity: 1;\n    background-image: url('/static/others/trash.svg') !important;\n}\n.dzu-previewImage {\n    max-height: 200px;\n    max-width: 200px;\n    padding: 0cqmax;\n    width: unset;\n    margin-top: 30px;\n    border: inherit;\n}\n\n"]))),N=e=>{let{images:s,setImages:a,articleImagesCount:l=0}=e;const{translate:r}=(0,t.useContext)(j.O);return(0,b.jsx)(b.Fragment,{children:(0,b.jsxs)(v,{onClick:()=>{0===s.length&&document.querySelector(".dzu-inputLabel").click()},className:0===s.length?"cursor-pointer":"",children:[(0,b.jsx)(f(),{inputContent:"",inputWithFilesContent:"+",maxFiles:20-l,onChangeStatus:(e,s)=>{let{file:l}=e;"done"===s&&console.log(l),"done"===s&&a((e=>[...e,l])),"removed"===s&&a((e=>e.filter((e=>e!==l))))},accept:"image/*"}),0===s.length&&(0,b.jsx)("div",{className:"text-center pt-3 d-flex align-items-center justify-content-center",style:{height:120},children:(0,b.jsx)("i",{style:{fontSize:100},className:"fa-solid fa-cloud-arrow-up fa-2xl color-theme"})}),(0,b.jsx)("h6",{className:"text-center color-theme p-3",children:s.length+l===0?r("Upload up to 20 images"):" ".concat(20-s.length-l," ")+r("images left")})]})})};var w=a(7664),y=a(508);const C=(new Date).getFullYear(),S=Array.from({length:C-1900+1},((e,s)=>1900+s)),k=()=>{const{translate:e}=(0,t.useContext)(j.O);let{browserData:s,setGlobalMessage:a,transformedParameters:l}=(0,t.useContext)(r._);const[u,p]=(0,t.useState)(1),{userData:f}=(0,t.useContext)(n.S),{articleId:g}=(0,h.UO)(),[v,k]=(0,t.useState)(),[_,z]=(0,t.useState)([]),[L,Z]=(0,t.useState)(0),[F,E]=(0,t.useState)(!1),A=(0,t.useRef)();(0,t.useEffect)((()=>{g&&(E(!0),d.Z.get("/api/dashboard/get-article-for-edit/?article-id="+g,{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+f.token}}).then((e=>{A.current.classList.remove("error");let s=e.data;B(s.state_code),M(s.city),O(s.title),R(Number(s.brand_id)),U(s.other_brand),G(Number(s.category_id)),V(s.other_category),K(s.year),Q(s.color_id),$(s.document_id),se(s.engine),le(s.price),re(s.offered_price),ie(s.is_used?"Used":"New"),ce(s.mileage),me(s.fuel_id),xe(s.gear_box_id),pe(s.exchange),ge(s.is_all_options),be(l.options.filter((e=>s.options.includes(e.value)))),Ne(s.description);const[a,t,r]=s.phone_numbers_list;a&&ye(a),t&&Se(t),r&&_e(r),z(s.images_list),Z(s.main_image_id),E(!1)})).catch((e=>{E(!1),Le(e)})))}),[g]);const[I,B]=(0,t.useState)("16"),[D,M]=(0,t.useState)(""),[T,O]=(0,t.useState)(""),[P,R]=(0,t.useState)(1),[W,U]=(0,t.useState)(""),[Y,G]=(0,t.useState)(1),[q,V]=(0,t.useState)(""),[H,K]=(0,t.useState)(C),[J,Q]=(0,t.useState)("1"),[X,$]=(0,t.useState)("1"),[ee,se]=(0,t.useState)(""),[ae,le]=(0,t.useState)(0),[te,re]=(0,t.useState)(0),[ne,ie]=(0,t.useState)("Used"),[oe,ce]=(0,t.useState)(0),[de,me]=(0,t.useState)("1"),[he,xe]=(0,t.useState)("1"),[ue,pe]=(0,t.useState)(!1),[fe,ge]=(0,t.useState)(!1),[je,be]=(0,t.useState)([]),[ve,Ne]=(0,t.useState)(""),[we,ye]=(0,t.useState)(""),[Ce,Se]=(0,t.useState)(""),[ke,_e]=(0,t.useState)(""),[ze,Le]=(0,t.useState)(null),{loadingCreateArticle:Ze,setLoadingCreateArticle:Fe}=(0,t.useContext)(n.S),Ee=(0,h.s0)(),Ae={allItemsAreSelected:e("All options are selected"),clearSearch:e("Clear Search"),clearSelected:e("Clear Selected options"),noOptions:e("No options"),search:e("Search"),selectAll:e("Select all"),selectAllFiltered:e("Select all (filtered)"),selectSomeItems:e("Select..."),create:e("Create")},[Ie,Be]=(0,t.useState)([]),[De,Me]=(0,t.useState)(!1),{Left:Te,Right:Oe,S:Pe}=(0,t.useContext)(r._),Re=(0,t.useRef)(),We=(0,t.useRef)();let Ue=!1;T.trim()?A.current&&A.current.classList.remove("error"):(A.current&&A.current.classList.add("error"),Ue=!0),10==Y&&""==q.trim()?(Re.current&&Re.current.classList.add("error"),Ue=!0):Re.current&&Re.current.classList.remove("error"),93==P&&""==W.trim()?(We.current&&We.current.classList.add("error"),Ue=!0):We.current&&We.current.classList.remove("error");const Ye=(0,t.useContext)(r._);return(0,t.useEffect)((()=>{g?Ye.setTitle(e("Edit article")+" | ".concat(e("Ch7al Machya"))):Ye.setTitle(e("Create article")+" | ".concat(e("Ch7al Machya"))),Ye.setDescription(e("description"))}),[]),(0,b.jsxs)(b.Fragment,{children:[(0,b.jsx)("div",{hidden:!F,className:"container mw-900",children:(0,b.jsx)("div",{className:"card mt-5 py-5",children:(0,b.jsx)(o.a,{className:"color-theme my-5 m-auto",diam:80})})}),(0,b.jsx)("div",{hidden:F,className:"pb-5",children:(0,b.jsxs)(c.Z,{className:"mt-5 mw-900",children:[ze&&(0,b.jsx)(i.v,{variant:"danger",removeAlert:()=>{Le(null)},children:ze.response.data.detail||ze.message}),v&&(0,b.jsx)(i.v,{variant:"success",removeAlert:()=>{k(null)},children:v}),(0,b.jsxs)("div",{className:Ze?"blur":"",children:[(0,b.jsxs)("div",{hidden:1!==u,className:"d-flex flex-row flex-wrap",children:[(0,b.jsxs)("div",{id:"state",className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("State")})}),(0,b.jsx)("select",{className:"form-select",onChange:e=>B(e.target.value),value:I,children:s.states.map((e=>(0,b.jsxs)("option",{value:e.code,children:[e.code," ",e.name]},e.code)))})]}),(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("City")})}),(0,b.jsx)("input",{className:"form-control",type:"text",placeholder:e("Enter city"),value:D,onChange:e=>{let s=e.target.value;M(s)},maxLength:50})]}),(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsxs)("strong",{children:[e("Phone number")," 1"]})}),(0,b.jsx)("input",{className:"form-control",type:"tel",placeholder:e("You can keep this field empty"),value:we,onChange:e=>{let s=e.target.value;(0,m.xT)(s)&&ye(s)}})]}),(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsxs)("strong",{children:[e("Phone number")," 2"]})}),(0,b.jsx)("input",{className:"form-control",type:"tel",placeholder:e("You can keep this field empty"),value:Ce,onChange:e=>{let s=e.target.value;(0,m.xT)(s)&&Se(s)}})]}),(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsxs)("strong",{children:[e("Phone number")," 3"]})}),(0,b.jsx)("input",{className:"form-control",type:"tel",placeholder:e("You can keep this field empty"),value:ke,onChange:e=>{let s=e.target.value;(0,m.xT)(s)&&_e(s)}})]})]}),(0,b.jsxs)("div",{hidden:2!==u,children:[(0,b.jsx)("div",{className:"col-12 col-sm-6",children:(0,b.jsx)(w.Z,{emptySelection:!0,category:Y,setCtegory:G})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap p".concat(Pe,"-4 col-12 col-sm-6"),hidden:10!=Y,children:(0,b.jsx)("div",{className:"form-group mt-2 p-2 flex-grow-1",ref:Re,children:(0,b.jsx)("input",{className:"form-control",type:"text",placeholder:e("Enter category name"),value:q,onChange:e=>{V(e.target.value)},maxLength:50})})}),(0,b.jsx)("div",{className:"col-12 col-sm-6",children:(0,b.jsx)(y.Z,{emptySelection:!0,category:Y,setBrand:R,brand:P})}),(0,b.jsx)("div",{hidden:93!=P,className:"d-flex flex-row flex-wrap p".concat(Pe,"-4 col-12 col-sm-6"),children:(0,b.jsx)("div",{className:"form-group mt-2 p-2 flex-grow-1",ref:We,children:(0,b.jsx)("input",{className:"form-control",type:"text",placeholder:e("Enter brand name"),value:W,onChange:e=>{U(e.target.value)},maxLength:50})})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",ref:A,children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsxs)("strong",{children:[e("Model")," *"]})}),(0,b.jsx)("input",{className:"form-control",type:"text",placeholder:e("Enter car model"),value:T,onChange:e=>{O(e.target.value)},maxLength:50})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Year")})}),(0,b.jsx)("select",{className:"form-select",value:H,onChange:e=>{let s=e.target.value;K(s)},children:S.map((e=>(0,b.jsx)("option",{children:e},e)))})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Color")})}),(0,b.jsx)("select",{className:"form-select",value:J,onChange:e=>{let s=e.target.value;Q(s)},children:s.colors.map((e=>(0,b.jsx)("option",{value:e.id,children:e.name},e.id)))})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Engine")})}),(0,b.jsx)("input",{className:"form-control",type:"text",placeholder:e("Enter engine detail"),value:ee,onChange:e=>{let s=e.target.value;se(s)},maxLength:50})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Car condtion")})}),(0,b.jsxs)("select",{className:"form-select",value:ne,onChange:e=>{let s=e.target.value;ie(s)},children:[(0,b.jsx)("option",{children:e("Used")}),(0,b.jsx)("option",{children:e("New")})]})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Mileage (in KM)")})}),(0,b.jsx)("input",{className:"form-control",type:"number",value:oe,onChange:e=>{let s=e.target.value;ce(s)},min:0})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Fuel")})}),(0,b.jsx)("select",{className:"form-select",value:de,onChange:e=>{let s=e.target.value;me(s)},children:s.fuels.map((e=>(0,b.jsx)("option",{value:e.id,children:e.name},e.id)))})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Gearbox")})}),(0,b.jsx)("select",{className:"form-select",value:he,onChange:e=>{let s=e.target.value;xe(s)},children:s.gear_boxs.map((e=>(0,b.jsx)("option",{value:e.id,children:e.name},e.id)))})]})}),(0,b.jsx)("hr",{}),(0,b.jsxs)("div",{className:"form-group d-flex m-3  align-items-center",children:[(0,b.jsx)("strong",{className:"fs-5",children:e("Is it fully loaded ?")}),(0,b.jsx)("input",{className:"mx-3",type:"checkbox",checked:fe,onChange:e=>{be([]);let s=e.target.checked;ge(s)}})]}),!fe&&(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("If not what are its options ?")})}),(0,b.jsx)(x.NU,{className:"hide-search",overrideStrings:Ae,options:s.options.map((e=>{let{id:s,name:a}=e;return{label:a,value:s}})),labelledBy:"Select",value:je,onChange:be})]})}),(0,b.jsx)("hr",{}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Document")})}),(0,b.jsx)("select",{className:"form-select",value:X,onChange:e=>{let s=e.target.value;$(s)},children:s.documents.map((e=>(0,b.jsx)("option",{value:e.id,children:e.name},e.id)))})]})}),(0,b.jsxs)("div",{className:"form-group d-flex m-3  align-items-center",children:[(0,b.jsx)("strong",{className:"fs-5",children:e("Open for exchange?")}),(0,b.jsx)("input",{className:"mx-3",type:"checkbox",checked:ue,onChange:e=>{let s=e.target.checked;pe(s)}})]})]}),(0,b.jsxs)("div",{hidden:3!==u,children:[(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Price (in Millions)")})}),(0,b.jsx)("input",{className:"form-control",type:"number",value:ae,onChange:e=>{let s=e.target.value;le(s)},min:0})]})}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12 col-sm-6 p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Offred Price (in Millions)")})}),(0,b.jsx)("input",{className:"form-control",type:"number",value:te,onChange:e=>{let s=e.target.value;re(s)},min:0})]})}),(0,b.jsx)("hr",{}),(0,b.jsx)("div",{className:"d-flex flex-row flex-wrap",children:(0,b.jsxs)("div",{className:"form-group mt-2 col-12  p-2",children:[(0,b.jsx)("label",{className:"form-label",children:(0,b.jsx)("strong",{children:e("Description")})}),(0,b.jsx)("textarea",{rows:5,className:"form-control",type:"text",value:ve,onChange:e=>{let s=e.target.value;Ne(s)}})]})})]}),(0,b.jsxs)("div",{hidden:4!==u,children:[g&&(0,b.jsxs)(b.Fragment,{children:[(0,b.jsx)("h3",{className:"mb-4 color-theme",children:e("Current Images")}),(0,b.jsxs)("div",{className:"d-flex mb-5 border rounded-3 p-3 flex-wrap gap-2 justify-content-around",children:[_.find((e=>e.id==L))&&(0,b.jsx)("div",{className:"mb-5",children:(0,b.jsxs)("div",{className:"square border rounded-2",style:{width:200,marginTop:54},children:[(0,b.jsxs)("button",{type:"btn",style:{[Te]:5,top:5},className:"btn btn-success btn-sm position-absolute z-1",children:[" ",(0,b.jsx)("i",{className:"fa-solid fa-thumbtack fa-xl"})]}),(0,b.jsx)("img",{className:"rounded-1 ".concat(De&&" blur"),src:"/resized-image/200/?path=".concat(_.find((e=>e.id==L)).url.slice(1))})]})}),_.filter((e=>e.id!=L)).map((e=>(0,b.jsxs)("div",{className:"mb-5",children:[(0,b.jsxs)("div",{className:"d-flex justify-content-between",children:[(0,b.jsx)("div",{children:e.id!=L&&(0,b.jsx)("button",{disabled:De,onClick:()=>{(e=>{Me(!0),d.Z.post("/api/dashboard/set-main-image/",{image_id:e,article_id:g},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+f.token}}).then((e=>{Z(e.data),Me(!1)})).catch((e=>{Me(!1)}))})(e.id)},className:"btn btn-outline-success m-2 p-1 px-2 rounded-1 border-0",children:(0,b.jsx)("i",{className:"fa-solid fa-thumbtack fa-xl"})})}),(0,b.jsxs)("div",{children:[(0,b.jsx)("button",{hidden:1==_.length,type:"button",disabled:De,onClick:()=>(e=>{Me(!0),d.Z.post("/api/dashboard/delete-image/",{image_id:e,article_id:g},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+f.token}}).then((e=>{z((s=>s.filter((s=>s.id!=e.data)))),Me(!1)})).catch((e=>{Me(!1)}))})(e.id),className:"m-2 btn btn-outline-danger p-1 rounded-1 border-0",children:(0,b.jsx)("i",{className:"fa-solid fa-trash fa-xl"})}),"                        "]})]}),(0,b.jsx)("div",{className:"square border rounded-2 ".concat(e.id==L&&"overlow-hidden border-3 border-success"),style:{width:200},children:(0,b.jsx)("img",{className:"rounded-2 ".concat(De&&" blur"),src:"/resized-image/200/?path=".concat(e.url.slice(1))})},e.id)]},e.id)))]}),(0,b.jsx)("h3",{className:"mb-4 mt-5 color-theme",children:e("Add Images")})]}),(0,b.jsx)(N,{articleImagesCount:_.length,images:Ie,setImages:Be})]})]}),(0,b.jsxs)("div",{className:"d-flex col-12 py-4",children:[u>=2&&(0,b.jsx)("button",{type:"submit",className:"w-fit-content d-flex btn btn-success",disabled:Ze,onClick:e=>{e.preventDefault(),u>=2&&p((e=>e-1)),(0,m.k3)()},children:(0,b.jsxs)("span",{children:[(0,b.jsx)("i",{className:"fa-solid fa-chevron-".concat(Te)})," ",e("Go back")]})}),(0,b.jsx)("button",{type:"submit",disabled:2===u&&Ue||4===u&&Ie.length+_.length===0||Ze,className:"w-fit-content d-flex btn btn-success margin-inline-start-auto",onClick:s=>{s.preventDefault(),u<=4&&(u<4?((0,m.k3)(),p((e=>e+1))):(async s=>{k(null),Le(null),s.preventDefault(),Fe(!0),a({text:e("Your article is loading..."),variant:"success"});const l=window.location.href;d.Z.post(g?"/api/dashboard/update-article/":"/api/dashboard/create-article/",{state:I,city:D,title:T,brand:P,other_brand:W,category:Y,other_category:q,year:H,color:J,document:X,engine:ee,price:ae,offered_price:te,car_condition:ne,mileage:oe,fuel:de,gear_box:he,exchange:ue,all_options_car:fe,car_options:je.map((e=>e.value)),description:ve,phone_number_1:we,phone_number_2:Ce,phone_number_3:ke,images:await(0,m.IG)(Ie),article_id:g},{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+f.token}}).then((e=>{if(Fe(!1),a(null),"Notification"in window){var s=new Notification(f.extention.is_page?f.page.name:"".concat(f.profile.first_name," ").concat(f.profile.last_name),{body:e.data.detail.message,icon:f.extention.image_150});s.onclick=()=>{Ee("/redirect/?redirect=".concat(e.data.detail.url)),s.close()}}l==window.location.href&&Ee(e.data.detail.url)})).catch((e=>{Fe(!1),Le(e)}))})(s))},children:4===u?Ze?(0,b.jsxs)(b.Fragment,{children:[e("Getting Created")," ",(0,b.jsx)(o.a,{className:"mx-2",diam:23})]}):(0,b.jsx)(b.Fragment,{children:e(g?"Update article":"Create article")}):(0,b.jsxs)("span",{children:[e("Next")," ",(0,b.jsx)("i",{className:"fa-solid fa-chevron-".concat(Oe)})]})})]})]})})]})}}}]);
//# sourceMappingURL=746.34826bfd.chunk.js.map