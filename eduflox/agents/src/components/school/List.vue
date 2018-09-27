<template>
<div>
  <div class="columns is-multiline">
    <div id="app" class="column">
      <button class="button is-primary" @click="resetForm(); isModalFormActive = true">
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
import { Actions, TableColumns } from "../../store/constants";

export default {
  name: "VSchool",
  components: {
    VSchoolForm
  },
  created() {
    this.$store.dispatch(Actions.GetAllSchools);
  },
  data() {
    return {
      selected: null,
      columns: TableColumns.SchoolTableColumns,
      isModalFormActive: false
    };
  },
  computed: {
    ...mapState({
      loading: state => state.loading,
      schools: state => state.schools
    })
  },
  methods: {
    resetForm() {
      this.selected = null;
    }
  }
};
</script>
