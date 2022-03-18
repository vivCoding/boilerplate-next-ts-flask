import { Box, Container, Typography } from '@mui/material'
import type { NextPage } from 'next'
import Image from 'next/image'
import Helmet from '../components/common/Helmet'

const Home: NextPage = () => (
  <Container sx={{ m: 2 }}>
    <Helmet title="Hello World" />
    <Typography variant="h3">Hello world</Typography>
    <Box sx={{ my: 4 }}>
      <Image src="/cat_typing_fast.gif" alt="super fast typing cat" width={300} height={300} />
    </Box>
    <Typography>I daresay this is pretty cool</Typography>
  </Container>
)

export default Home
