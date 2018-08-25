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
        <v-school-form v-bind="schoolForm"></v-school-form>
      </b-modal>
    </div>
  </div>
 </div>
</template>

<script>
import VSchoolForm from "./Form";

export default {
  name: "VSchool",
  components: {
    VSchoolForm
  },
  data() {
    return {
      schools: [],
      columns: [
        { field: "name", label: "Name", sortable: true },
        { field: "code", label: "Code", sortable: true },
        { field: "location", label: "Location", sortable: true },
        { field: "district", label: "District", sortable: true },
        { field: "status", label: "Status", sortable: true },
        {
          field: "created_at",
          label: "Date Created",
          sortable: true,
          centered: true
        }
      ],
      selected: null,
      loading: false,
      isModalFormActive: false,
      schoolForm: {
        name: "",
        code: "",
        location: "",
        district: ""
      }
    };
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
