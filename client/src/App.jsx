import { useState, useEffect } from 'react'
import './App.css'
import axios from "axios"

function App() {
  const [count, setCount] = useState(0)

  const fetchAPI_GPT = async () => {
    const response = await axios.get("http://127.0.0.1:8080/analyze_video_gpt")
    console.log(response)
  }
  const fetchAPI_VADER = async () => {
    const response = await axios.get("http://127.0.0.1:8080/analyze_video_vader")
    console.log(response)
  }
  useEffect(() => {
      fetchAPI_GPT()
      fetchAPI_VADER()

    }, [])
  

  return (
    <>
      <h1>Sentiment analysis</h1>
      <p>currently data is in console. Project under development</p>
    </>
  )
}

export default App
