interface Props{
 value:string
 setValue:(v:string)=>void
}

export default function ModelSelector({value,setValue}:Props){

 return(
  <select
   value={value}
   onChange={(e)=>setValue(e.target.value)}
   style={{
    padding:10,
    borderRadius:8,
    border:"1px solid #d1d5db"
   }}
  >
    <option value="ollama">Ollama</option>
  </select>
 )
}