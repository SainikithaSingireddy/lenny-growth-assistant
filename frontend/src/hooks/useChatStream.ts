"use client";

import { useState } from "react";
import { askQuestion } from "../lib/api";

export interface ChatMessage{
 role:"user"|"assistant";
 content:string;
}

export function useChatStream(){

 const [messages,setMessages]=useState<ChatMessage[]>([]);
 const [artifact,setArtifact]=useState("");
 const [loading,setLoading]=useState(false);

 async function send(message:string,provider:string){

  if(!message.trim()) return;

  setMessages(prev=>[
   ...prev,
   {role:"user",content:message}
  ]);

  setLoading(true);

  const data=await askQuestion(message,provider);

  setMessages(prev=>[
   ...prev,
   {role:"assistant",content:data.answer}
  ]);

  setArtifact(data.artifact_html);

  setLoading(false);
 }

 return{
  messages,
  loading,
  artifact,
  send
 };
}