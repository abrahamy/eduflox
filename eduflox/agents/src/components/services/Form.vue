<template>
<form ref="form" action="">
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">{{ titleText }}</p>
      <a href="#" class="card-header-icon" @click.prevent="$parent.close()">
        <b-icon icon='close'/>
      </a>
    </header>
    <section class="modal-card-body">

      <b-field label="School">
        <b-select v-model="form.school" placeholder="Select a school" expanded required>
          <option v-for="school in schools" :key="school.id" :value="school.id">
            {{ school.name }}
          </option>
        </b-select>
      </b-field>

      <b-field label="Description">
        <b-input v-model="form.service_description" type="textarea" placeholder="Describe the service desired." required></b-input>
      </b-field>

    </section>
    <footer class="modal-card-foot">
      <button class="button" type="button" @click="$parent.close()">Close</button>
      <button class="button is-primary" type="submit" @click.prevent="saveForm">Submit</button>
    </footer>
  </div>
</form>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { Actions } from "../../store/constants";
export default {
  name: "VServiceForm",
  props: {
    service: {
      type: Object,
      default() {
        return {};
      }
    }
  },
  data() {
    return {
      form: {
        ...this.$props.service
      }
    };
  },
  computed: {
    ...mapState({
      schools: state => state.schools
    }),
    isEditing() {
      return this.$props.service && this.$props.service.id;
    },
    titleText() {
      return this.isEditing ? "Edit Request" : "Service Request";
    }
  },
  methods: {
    ...mapActions({
      addNewService: Actions.AddNewService,
      updateExistingService: Actions.UpdateExistingService,
      sendError: Actions.SendError
    }),
    saveForm() {
      if (this.$refs.form.checkValidity()) {
        let data = { ...this.form };
        if (this.isEditing) {
          this.updateExistingService(data);
        } else {
          this.addNewService(data);
        }
        this.$parent.close();
        return;
      }
      this.$toast.open({
        duration: 3000,
        message: "Please complete all fields.",
        position: "is-top",
        type: "is-danger"
      });
    }
  }
};
</script>
