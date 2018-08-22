import Vue from 'vue'
import Buefy from 'buefy'
import AppView from './App'
import SchoolListView from './school/List'
import '@mdi/font/css/materialdesignicons.min.css'
import '../assets/scss/app.scss'

Vue.use(Buefy)

const components = [
  AppView,
  SchoolListView
]

export default components
