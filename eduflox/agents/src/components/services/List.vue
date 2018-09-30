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
        :data="services"
        :loading="loading"
        paginated
        pagination-simple
        hoverable
        striped>
        <template slot-scope="props">
          <b-table-column field="school" label="School" sortable>
            {{ props.row.school }}
          </b-table-column>
          <b-table-column field="service_description" label="Description" sortable>
            {{ props.row.service_description }}
          </b-table-column>
          <b-table-column field="created_at" label="Date Created" sortable>
            {{ $moment(props.row.created_at).format('LL') }}
          </b-table-column>
          <b-table-column label="">
            <p class="buttons">
              <a class="button is-info is-outlined" @click.prevent="editRow(props.row)">
                <b-icon icon="pencil"></b-icon>
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
        <v-service-form :service="selected"/>
      </b-modal>
    </div>
  </div>
 </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import VServiceForm from "./Form";
import { Actions } from "../../store/constants";

export default {
  name: "VService",
  components: {
    VServiceForm
  },
  created() {
    this.getAllSchools();
  },
  mounted() {
    this.getAllServices();
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
      services: state => state.services
    })
  },
  methods: {
    ...mapActions({
      getAllServices: Actions.GetAllServices,
      getAllSchools: Actions.GetAllSchools,
      deleteService: Actions.DeleteExistingService
    }),
    editRow(service) {
      this.selected = service;
      this.isModalFormActive = true;
    },
    deleteRow(service) {
      this.$dialog.confirm({
        title: "Confirm Action",
        message: `Are you sure you want to <b>delete</b> the service? This action cannot be undone.`,
        confirmText: "Delete",
        type: "is-danger",
        hasIcon: true,
        onConfirm: () => {
          this.deleteService(service);
          setTimeout(() => {
            this.$toast.open("Service deleted!");
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
