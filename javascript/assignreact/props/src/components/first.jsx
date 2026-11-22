import React from 'react'

const first = (props) => {
  return (
    <div>
        <h1>first component (child component)</h1>
        <p>{props.dataMsg}</p>
        <Second/>
    </div>
  )
}

export default first ;
