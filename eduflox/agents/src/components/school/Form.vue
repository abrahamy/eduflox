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
        <b-input v-model="form.name" placeholder="Name of School" required/>
      </b-field>
      <b-field label="Location">
        <b-input v-model="form.location" placeholder="Ikeja" :readonly="isEditing" required/>
      </b-field>
      <b-field label="District">
        <b-input v-model="form.district" placeholder="Lagos" required/>
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
import { mapActions } from "vuex";
import { Actions } from "../../store/constants";
export default {
  name: "VSchoolForm",
  props: {
    school: {
      type: Object,
      default() {
        return {};
      }
    }
  },
  data() {
    return {
      form: {
        ...this.$props.school
      }
    };
  },
  computed: {
    isEditing() {
      return this.$props.school && this.$props.school.id;
    },
    titleText() {
      return this.isEditing ? "Edit School" : "New School";
    }
  },
  methods: {
    ...mapActions({
      addNewSchool: Actions.AddNewSchool,
      updateExistingSchool: Actions.UpdateExistingSchool,
      sendError: Actions.SendError
    }),
    saveForm() {
      if (this.$refs.form.checkValidity()) {
        let data = { ...this.form };
        if (this.isEditing) {
          this.updateExistingSchool(data);
        } else {
          this.addNewSchool(data);
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
