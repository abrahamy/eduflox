<template>
<form action="">
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Create New School</p>
      <a href="#" class="card-header-icon" @click.prevent="$parent.close()">
        <b-icon icon='close'/>
      </a>
    </header>
    <section class="modal-card-body">
      <b-notification type="is-danger" :active="showNotification" has-icon>
        {{ message }}
      </b-notification>

      <b-field label="School">
        <b-input v-model="form.name" placeholder="Name of School" required/>
      </b-field>
      <b-field label="Location">
        <b-input v-model="form.location" placeholder="Ikeja" required/>
      </b-field>
      <b-field label="District">
        <b-input v-model="form.district" placeholder="Lagos" required/>
      </b-field>
    </section>
    <footer class="modal-card-foot">
      <button class="button" type="button" @click="$parent.close()">Close</button>
      <button class="button is-primary" type="submit" @click="saveForm">Submit</button>
    </footer>
  </div>
</form>
</template>

<script>
import { Actions } from "../../store/constants";
export default {
  name: "VSchoolForm",
  props: {
    school: {
      type: Object,
      required: false
    }
  },
  data() {
    let school = this.$props.school || {};
    return {
      form: {
        ...school
      },
      message: ""
    };
  },
  computed: {
    showNotification() {
      return (this.message || "").length ? true : false;
    }
  },
  methods: {
    saveForm() {
      this.$store.dispatch(Actions.AddNewSchool, { ...this.form });
    }
  }
};
</script>
