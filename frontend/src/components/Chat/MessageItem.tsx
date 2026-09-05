interface Props{
  role:string
  content:string
}

export default function MessageItem({role,content}:Props){

  const isUser = role==="user";

  return(
    <div
      style={{
        display:"flex",
        justifyContent:isUser?"flex-end":"flex-start",
        marginBottom:12
      }}
    >
      <div
        style={{
          maxWidth:"75%",
          padding:14,
          borderRadius:12,
          background:isUser?"#2563eb":"#eef2ff",
          color:isUser?"white":"#111827"
        }}
      >
        {content}
      </div>
    </div>
  )
}