import './App.scss'
import Nav from './Components/Nav'
import Post from './Components/Post'
import Logout from './Components/Logout'
import TmpProfile from './Components/tmp/Profile'
import { useGetMeQuery } from './redux/api/me'
import TmpPost from './Components/tmp/Post'
import TmpArticle from './Components/tmp/Article'
import NewPost from './Screens/NewPost'


function App() {

  const { data: dataMe, isError, isLoading, error } = useGetMeQuery()

  return (
    <>
      <Nav />
      <main>
        <Post />
        <Logout />
        {dataMe && <TmpProfile userData={dataMe} />}
        <NewPost />
      </main>
    </>

  )
}

export default App
