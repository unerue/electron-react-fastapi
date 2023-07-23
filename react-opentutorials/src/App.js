import { useState } from 'react';
import './App.css';

function Header(props) {
  console.log('props', props, props.title)
  return (
    <div>
      <header><h1><a href="/" onClick={ (event) => {
        event.preventDefault();
        props.onChangeMode();
      } }>{ props.title }</a></h1></header>
    </div>
  );
}

function Nav(props) {
  const lis = []
  for (let i=0; i<props.topics.length; i++) {
    let t = props.topics[i];
    lis.push(<li key={ t.id }>
      <a id={ t.id } href={ '/read/'+t.id } onClick={(event)=>{
        event.preventDefault();
        props.onChangeMode(event.target.id)
      }}>{ t.title }</a>
    </li>);
  }
  return (
    <div>
      <nav>
        <ol>
          { lis }
        </ol>
      </nav>
    </div>
  );
}

function Article(props) {

  return (
    <div>
      <article>
        <h1>{ props.title }</h1>
        <p>{ props.body }</p>
      </article>
    </div>
  );
}

function App() {
  // const mode = 'WELCOME'
  const [mode, setMode] = useState('WELCOME');
  const topics = [
    {id: 1, title: 'html', body: 'html is ...'},
    {id: 2, title: 'css', body: 'css is ...'},
    {id: 3, title: 'javascript', body: 'javascript is ...'},
  ]

  let content = null;
  if (mode === 'WELCOME') {
    content = <Article title="Welcome" body="Hello, WEB"></Article>
  } else if (mode ==='READ') {
    content = <Article title="READ" body="hello, Read"></Article>
  }
  return (
    <div className="App">
      <Header title="REACT" onChangeMode={ () => {
        alert('Header');
        setMode('WELCOME');
      } }></Header>
      <Nav topics={topics} onChangeMode={ (id) => {
        alert(id);
        setMode('READ');
      } }></Nav>
      { content }
    </div>
  );
}

export default App;
