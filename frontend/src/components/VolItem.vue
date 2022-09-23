<template lang="">
  <div class="bg-white shadow sm:rounded-lg">
    <div class="px-4 py-5 sm:p-6">
      <h3 class="text-lg font-medium leading-6 text-gray-900">
        Vol #BV{{ fly.id }}
      </h3>
      <h5 class="text-md font-medium leading-6 text-gray-900">
        {{ priceVol }} 
      </h5>

      <div class="mt-2 sm:flex sm:items-start sm:justify-between">
        <div class="max-w-xl text-sm text-gray-500">
          <p>Départ : {{ fly.depart }}</p>
          <p>Destination: {{ fly.arrive }}</p>
        </div>
        
            <ButtonBook :IsButton="true"  :fly="fly"/>
      </div>
    </div>
   
  </div>
</template>
<script>
import { mapState } from "vuex";

import {
  TransitionChild,
  TransitionRoot,
  Dialog,
  DialogPanel,
  DialogTitle,
  Switch,
} from "@headlessui/vue";
  import { useToast } from "vue-toastification";
import ButtonBook  from "./ButtonBook.vue";

export default {
  components: {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
    Switch,
    ButtonBook
  },
  props: {
    fly: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      enabled: false,
      op: false,
      //total:null,
      isOpen: false,
      myReservation: {
        nom: "",
        prenom: "",
        nb_place: 1,
        vol:this.fly.id,
        code:this.fly.code,
        retour_inclut: false,
        date_depart: "",
        date_retour: "",
        first_class: false,
        champagne: false,
        currency:""
      },
    };
  },
  methods: {
    closeModal() {
      this.isOpen = false;
    },
    openModal() {
      this.isOpen = true;
    },
    ajouterUneReservation() {
        this.isOpen = false;
        const toast = useToast();
        this.myReservation.currency = this.currency;
        let res = null;
        if (this.fly.code) {
                  res = this.$store.dispatch("ajoutReservationExternal", this.myReservation);

        } else {
                  res = this.$store.dispatch("ajoutReservation", this.myReservation);

        }
        if (res) {
          toast.success("Merci ! Votre réservation a été enregistrée avec succès.");
        }
        else {
          toast.error("Error"+ res);

        }

    },
  },
  computed: {
    ...mapState(["currency"]),

    priceVol(){
      return this.currency === "EURO" ? this.fly.montant +" "+ this.currency: this.fly.price_map[this.currency ==='DOLLAR' ? 'USD' : 0 ] + " "+ this.currency
    },
    priceVolSimple(){
      return this.currency === "EURO" ? this.fly.montant : this.fly.price_map[this.currency === 'DOLLAR' ? 'USD' : 0 ] 
    },

    total() {
        let res = this.myReservation.nb_place * this.priceVolSimple
        this.myReservation.champagne ? res+=100 : null;
        this.myReservation.retour_inclut ? res*=2 :null;
        return res
    }
  }
};
</script>
<style lang=""></style>