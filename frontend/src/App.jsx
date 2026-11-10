import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [expression, setExpression] = useState('')
  const [result, setResult] = useState(null)
  const [history, setHistory] = useState([])

  const API_URL = 'http://localhost:8000'

  const fetchHistory = async () => {
    const res = await axios.get(`${API_URL}/history/`)
    setHistory(res.data)
  }

  useEffect(() => {
    fetchHistory()
  }, [])

  const handleCalculate = async (e) => {
    e.preventDefault()
    try {
      const res = await axios.post(`${API_URL}/calculate/?expression=${encodeURIComponent(expression)}`)
      setResult(res.data.result)
      fetchHistory()
    } catch (error) {
      alert("Error calculating expression")
    }
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>DevOps Calculator</h2>
      <form onSubmit={handleCalculate}>
        <input
          type="text"
          value={expression}
          onChange={(e) => setExpression(e.target.value)}
          placeholder="e.g., 5 + 10 * 2"
          required
        />
        <button type="submit">Calculate</button>
      </form>
      {result !== null && <h3>Result: {result}</h3>}

      <h4>Calculation History</h4>
      <ul>
        {history.map((item) => (
          <li key={item.id}>{item.expression} = {item.result} </li>
        ))}
      </ul>
    </div>
  )
}

export default App