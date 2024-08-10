import Form from './Form';
import Banner from './Banner';

function App() {
  const title = 'The New York Times'
  const subtitle = 'Front Page API'

  return (
    <div className="App">
        <Banner />
      <div className='content'>
        <div className="heading">
          <h1>{title}</h1>
          <h2>{subtitle}</h2>
          <Form />
        </div>
      </div>
    </div>
  );
}

export default App;
