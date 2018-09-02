<template>
<div>
  <div class="columns is-multiline">
    <div id="app" class="column">
      <button class="button is-primary" @click="isModalFormActive = true">
        <b-icon size="is-small" icon="plus"/>&nbsp;&nbsp;New
      </button>
      <br/>

      <!-- school list -->
      <b-table :data="schools" :columns="columns" :selected.sync="selected" focusable></b-table>

      <!-- school registration form -->
      <b-modal :active.sync="isModalFormActive" :canCancel="false" :onCancel="resetForm" has-modal-card>
        <v-school-form :school="selected"/>
      </b-modal>
    </div>
  </div>
 </div>
</template>

<script>
import { mapState } from "vuex";
import VSchoolForm from "./Form";
import * as K from "../../store/constants";

export default {
  name: "VSchool",
  components: {
    VSchoolForm
  },
  created() {
    this.$store.dispatch(K.SCHOOL_INIT);
    this.$store.dispatch(K.FETCH_SCHOOLS);
  },
  data() {
    return {
      selected: null,
      loading: false,
      isModalFormActive: false
    };
  },
  computed: {
    ...mapState({
      columns: state => state.columns,
      schools: state => state.schools
    })
  },
  methods: {
    resetForm() {
      let emptyForm = {};
      Object.keys(this.schoolForm).map(key => {
        emptyForm[key] = "";
      });
      this.schoolForm = emptyForm;
    }
  }
};
</script>
