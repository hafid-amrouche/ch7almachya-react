"use strict";(self.webpackChunkfe=self.webpackChunkfe||[]).push([[372],{9858:(e,s,t)=>{t.d(s,{Z:()=>r});t(2791);var a=t(184);const r=()=>(0,a.jsx)("div",{className:"col-12 col-sm-6 col-md-4 col-lg-3 p-1",children:(0,a.jsxs)("div",{className:"card",children:[(0,a.jsx)("div",{className:"main-image cursor-pointer mb-0",style:{backgroundColor:"var(--grey)",width:"100%",minWidth:150}}),(0,a.jsxs)("div",{className:"d-flex flex-column p-2 gap-1",children:[(0,a.jsx)("div",{className:"rounded bg-color-grey",style:{width:"80%",height:20}}),(0,a.jsx)("div",{className:"rounded bg-color-grey",style:{width:"60%",height:20}}),(0,a.jsx)("div",{className:"rounded bg-color-grey",style:{width:"40%",height:20}}),(0,a.jsx)("div",{className:"rounded bg-color-grey",style:{width:"50%",height:20}}),(0,a.jsx)("div",{className:"rounded bg-color-grey margin-inline-start-auto",style:{width:"40%",height:20}})]}),(0,a.jsx)("div",{className:"py-4"})]})})},7372:(e,s,t)=>{t.r(s),t.d(s,{default:()=>p});var a=t(2791),r=t(152),c=t(1767),l=t(9858),i=t(8255),o=t(184);const d=()=>((0,a.useEffect)((()=>{const e=document.createElement("script");return e.src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6526457297514391",e.crossOrigin="anonymous",document.body.appendChild(e),()=>{document.body.removeChild(e)}}),[]),(0,a.useEffect)((()=>{"undefined"!==typeof window&&window.adsbygoogle&&window.adsbygoogle.push({})}),[]),(0,o.jsx)("ins",{className:"adsbygoogle",style:{display:"block"},"data-ad-client":"ca-pub-6526457297514391","data-ad-slot":"8677743746","data-ad-format":"auto","data-full-width-responsive":"true"})),n=()=>{const{loadingSearchedArticles:e,articles:s,loadArticles:t,isNext:n,loadingMoreArticles:h,setLoadingMoreArticles:g,APISearchParameters:m}=(0,a.useContext)(r.c);let u=0;const[x,p]=(0,a.useState)(null),{translate:y}=(0,a.useContext)(i.O);return(0,o.jsxs)("div",{className:"pb-5",children:[(0,o.jsx)("div",{className:"col-12 d-flex flex-row flex-wrap",children:e?(0,o.jsx)(o.Fragment,{children:Array.from({length:20},((e,s)=>s)).map((e=>(0,o.jsx)(l.Z,{},e)))}):0===s.length?(0,o.jsx)("div",{className:"my-5 mx-auto",children:(0,o.jsx)("h3",{className:"my-4 text-center",children:y("No article was found.")})}):s.map((e=>(u+=1,(0,o.jsxs)(a.Fragment,{children:[u%7===0&&(0,o.jsx)("div",{className:"col-12 col-sm-6 col-md-4 col-lg-3 p-1",children:(0,o.jsxs)("div",{className:"card h-100 position-relative",children:[(0,o.jsx)("div",{className:"h-100 w-100",style:{position:"absolute",top:0},children:(0,o.jsx)(d,{})}),(0,o.jsx)("div",{style:{width:"100%",aspectRatio:1}}),(0,o.jsx)("div",{style:{height:170}})]})}),(0,o.jsx)(c.Z,{selectedArticle:x,setSelectedArticle:p,article:e})]},e.id))))}),n&&(0,o.jsx)("div",{className:"px-1",children:(0,o.jsx)("div",{className:"py-3 d-flex justify-content-center rounded-top-0",children:(0,o.jsx)("button",{disabled:h,onClick:()=>{g(!0),t(m.current)},className:"rounded-circle border border-3 bg-color-white border-dark w-fit-content aspect-ratio-1 p-3",children:(0,o.jsx)("i",{className:"fa-solid fa-plus fa-2xl"})})})})]})};var h=t(5294),g=t(4457),m=t(2046);const u=(0,a.lazy)((()=>t.e(778).then(t.bind(t,4778)))),x=(0,a.lazy)((()=>t.e(932).then(t.bind(t,8932)))),p=()=>{const[e,s]=(0,a.useState)([]),[t,c]=(0,a.useState)(!0),[l,d]=(0,a.useState)(!1),p=(0,a.useRef)(!1),y=new URL(window.location),j=y.searchParams,f=(0,a.useRef)({}),{togglePopup:v}=(0,a.useContext)(m._),b=y.searchParams.get("searchcategory"),{setTitle:w,setDescription:N}=(0,a.useContext)(m._),{translate:A}=(0,a.useContext)(i.O);(0,a.useEffect)((()=>{w(j.get("searchtext")+" | ".concat(A("Ch7al Machya"))),N(A("description"))}),[y]);const S={articles:e,setArticles:s,loadingSearchedArticles:t,setLoadingSearchedArticles:c,loadArticles:function(t){let a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:e.map((e=>e.id));h.Z.post("/api/article/search-articles/",{search_text_words_list:JSON.stringify((0,g.Sv)(j.get("searchtext"))),search_text:j.get("searchtext"),filter_parameters:JSON.stringify(t),seen_articles:JSON.stringify(a)},{headers:{"Content-Type":"multipart/form-data"}}).then((e=>{s((s=>[...s,...e.data[0]])),p.current=e.data[1],c(!1),d(!1),v(!1)})).catch((e=>{c(!1),d(!1)}))},isNext:p.current,loadingMoreArticles:l,setLoadingMoreArticles:d,APISearchParameters:f};return console.log(b),(0,o.jsxs)(r.c.Provider,{value:S,children:["vehicles"===b&&(0,o.jsxs)(o.Fragment,{children:[(0,o.jsx)(u,{}),(0,o.jsx)(n,{})]}),("users"===b||"pages"===b)&&(0,o.jsx)(x,{})]})}},152:(e,s,t)=>{t.d(s,{c:()=>a});const a=(0,t(2791).createContext)({showFiltrationSidebar:!1,setShowFiltrationSidebar:()=>{},articles:[],setArticles:()=>{},loadingSearchedArticles:!0,setLoadingSearchedArticles:()=>{},loadArticles:()=>{},loadingMoreArticles:!1,setLoadingMoreArticles:()=>{},searchParameters:{},setSearchParameters:{},APISearchParameters:{},searchUsers:()=>{}})}}]);
//# sourceMappingURL=372.9321d7c3.chunk.js.map