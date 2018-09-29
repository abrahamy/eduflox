<template>
<div>
  <div class="columns is-multiline">
    <div id="app" class="column">
      <button class="button is-info" @click="resetForm(); isModalFormActive = true">
        <b-icon size="is-small" icon="playlist-plus"/>&nbsp;&nbsp;Create
      </button>
      <br/>

      <!-- school list -->
      <b-table
        :data="schools"
        :loading="loading"
        paginated
        pagination-simple
        hoverable
        striped>
        <template slot-scope="props">
          <b-table-column field="name" label="School" sortable>
            {{ props.row.name }}
          </b-table-column>
          <b-table-column field="code" label="Code" sortable>
            {{ props.row.code }}
          </b-table-column>
          <b-table-column field="location" label="Location" sortable>
            {{ props.row.location }}
          </b-table-column>
          <b-table-column field="district" label="District" sortable>
            {{ props.row.district }}
          </b-table-column>
          <b-table-column field="status" label="Status" sortable>
            {{ props.row.status }}
          </b-table-column>
          <b-table-column field="created_at" label="Date Created" sortable>
            {{ $moment(props.row.created_at).format('LL') }}
          </b-table-column>
          <b-table-column label="">
            <p class="buttons">
              <a class="button is-info is-outlined" @click.prevent="editRow(props.row)">
                <b-icon icon="pencil"></b-icon>
              </a>
              <a v-if="isAdmin" :class="getAdminButtonStyle(props.row)" @click.prevent="approveOrRejectSchool(props.row)">
                <b-icon :icon="getAdminButtonIcon(props.row)"></b-icon>
              </a>
              <a class="button is-danger is-outlined" @click.prevent="deleteRow(props.row)">
                <b-icon icon="delete"></b-icon>
              </a>
            </p>
          </b-table-column>
        </template>

        <template slot="empty">
          <section class="section">
            <div class="content has-text-grey has-text-centered">
              <p><b-icon icon="emoticon-sad" size="is-large"></b-icon></p>
              <p>Nothing here.</p>
            </div>
          </section>
        </template>
      </b-table>

      <!-- school registration form -->
      <b-modal :active.sync="isModalFormActive" :canCancel="false" :onCancel="resetForm" has-modal-card>
        <v-school-form :school="selected"/>
      </b-modal>
    </div>
  </div>
 </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import VSchoolForm from "./Form";
import { Actions, Status } from "../../store/constants";

export default {
  name: "VSchool",
  components: {
    VSchoolForm
  },
  created() {
    this.getAllSchools();
  },
  data() {
    return {
      selected: null,
      isModalFormActive: false
    };
  },
  computed: {
    ...mapState({
      isAdmin: state => state.isAdminUser,
      loading: state => state.loading,
      schools: state => state.schools
    })
  },
  methods: {
    ...mapActions({
      getAllSchools: Actions.GetAllSchools,
      deleteSchool: Actions.DeleteExistingSchool,
      approveOrRejectSchool: Actions.ApproveOrRejectSchool
    }),
    getAdminButtonIcon(school) {
      return school.status === Status.Approved
        ? "close-circle"
        : "check-circle";
    },
    getAdminButtonStyle(school) {
      let buttonStyle = "button is-outlined";
      if (school.status === Status.Approved) {
        buttonStyle += " is-warning";
      } else {
        buttonStyle += " is-success";
      }
      return buttonStyle;
    },
    editRow(school) {
      this.selected = school;
      this.isModalFormActive = true;
    },
    deleteRow(school) {
      this.$dialog.confirm({
        title: "Confirm Action",
        message: `Are you sure you want to <b>delete</b> ${
          school.name
        }? This action cannot be undone.`,
        confirmText: "Delete",
        type: "is-danger",
        hasIcon: true,
        onConfirm: () => {
          this.deleteSchool(school);
          setTimeout(() => {
            this.$toast.open("School deleted!");
          }, 3000);
        }
      });
    },
    resetForm() {
      this.selected = null;
    }
  }
};
</script>
