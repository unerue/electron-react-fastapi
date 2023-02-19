import { useState } from 'react';
import './App.css';

function Modal() {
  return (
    <div className="modal">
      <h4>Post Title</h4>
      <p>Post date</p>
      <p>Post content</p>
    </div>
  );
}

function App() {
  let [checkLike, setCheckLike] = useState(0);

  return (
    <div className="App">
      <div className="black-nav">
        <h2>Hello!!</h2>
      </div>
      <div className="list">
        <h4>{}<span onClick={ () => { setCheckLike(1) }}>Like</span> { checkLike } </h4>
        <p></p>
      </div>
    </div>
  );
}

export default App;
