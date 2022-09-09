<template lang="">
  <div class="bg-white shadow sm:rounded-lg">
    <div class="px-4 py-5 sm:p-6">
      <h3 class="text-lg font-medium leading-6 text-gray-900">
        Vol #BV{{ fly.id }}
      </h3>
      <h5 class="text-md font-medium leading-6 text-gray-900">
        {{ fly.montant }} $
      </h5>

      <div class="mt-2 sm:flex sm:items-start sm:justify-between">
        <div class="max-w-xl text-sm text-gray-500">
          <p>Départ : {{ fly.depart }}</p>
          <p>Destination: {{ fly.arrive }}</p>
        </div>
        <div
          class="mt-5 sm:mt-0 sm:ml-6 sm:flex sm:flex-shrink-0 sm:items-center"
        >
          <button
            type="button"
            @click="openModal"
            class="inline-flex items-center rounded-md border border-transparent bg-blue-600 px-4 py-2 font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 sm:text-sm"
          >
            Book
          </button>
        </div>
      </div>
    </div>
    <TransitionRoot appear :show="isOpen" as="template">
      <Dialog as="div" @close="closeModal" class="relative z-10">
        <TransitionChild
          as="template"
          enter="duration-300 ease-out"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="duration-200 ease-in"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-black bg-opacity-25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
          <div
            class="flex min-h-full items-center justify-center p-4 text-center"
          >
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <DialogPanel
                class="w-full max-w-xl transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
              >
                <DialogTitle
                  as="h3"
                  class="text-lg font-medium leading-6 text-gray-900"
                >
                  Réservation
                </DialogTitle>
                <div class="mt-2">
                  <label>Vol: {{ fly.depart }} -> {{ fly.arrive }}</label> ====> {{total}}
                  <div class="pt-5">
                    <label
                      for="email"
                      class="block text-sm font-medium text-gray-700"
                      >Nom</label
                    >
                    <div class="mt-1">
                      <input
                        type="text"
                        class="block w-full px-3 py-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                        placeholder="Nom.."
                        v-model="myReservation.nom"
                      />
                    </div>
                  </div>

                  <div class="pt-5">
                    <label
                      for="email"
                      class="block text-sm font-medium text-gray-700"
                      >Prenom</label
                    >
                    <div class="mt-1">
                      <input
                        type="text"
                        name="email"
                        id="email"
                        class="block w-full px-3 py-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                        placeholder="Prenom.."
                        v-model="myReservation.prenom"
                      />
                    </div>
                  </div>

                  <div class="pt-5">
                    <label
                      for="email"
                      class="block text-sm font-medium text-gray-700"
                      >Nombre de Places</label
                    >
                    <div class="mt-1">
                      <input
                        type="number"
                        name="email"
                        id="email"
                        class="block w-full rounded-md px-3 py-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                        placeholder=""
                        v-model="myReservation.nbrPlace"
                      />
                    </div>
                  </div>

                  <div class="pt-5">
                    <label
                      for="email"
                      class="block text-sm font-medium text-gray-700 pb-2"
                      >Aller/Retour</label
                    >
                    <Switch
                      v-model="myReservation.retour_inclut"
                      :class="[
                        myReservation.retour_inclut
                          ? 'bg-blue-600'
                          : 'bg-gray-200',
                        'relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2',
                      ]"
                    >
                      <span class="sr-only">Use setting</span>
                      <span
                        aria-hidden="true"
                        :class="[
                          myReservation.retour_inclut
                            ? 'translate-x-5'
                            : 'translate-x-0',
                          'pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out',
                        ]"
                      />
                    </Switch>
                  </div>

                  <div
                    class="pt-5"
                    v-if="
                      (fly.depart == 'CDG' && fly.arrive == 'FJK') ||
                      (fly.depart == 'FJK' && fly.arrive == 'CDG')
                    "
                  >
                    <label
                      for="email"
                      class="block text-sm font-medium text-gray-700 pb-2"
                      >Option Champagne (+100$)</label
                    >

                    <Switch
                      v-model="myReservation.optionChampagne"
                      :class="[
                        myReservation.optionChampagne
                          ? 'bg-blue-600'
                          : 'bg-gray-200',
                        'relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2',
                      ]"
                    >
                      <span class="sr-only">Use setting</span>
                      <span
                        aria-hidden="true"
                        :class="[
                          myReservation.optionChampagne
                            ? 'translate-x-5'
                            : 'translate-x-0',
                          'pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out',
                        ]"
                      />
                    </Switch>
                  </div>

                  <div class="pt-5">
                    <label
                      for="email"
                      class="block text-sm font-medium text-gray-700"
                      >Date Départ</label
                    >
                    <div class="mt-1">
                      <input
                        type="date"
                        name="email"
                        id="email"
                        class="block w-full rounded-md px-3 py-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                        placeholder=""
                        v-model="myReservation.date_depart"
                      />
                    </div>
                  </div>
                  <div class="pt-5" v-if="myReservation.retour_inclut">
                    <label
                      for="email"
                      class="block text-sm font-medium text-gray-700"
                      >Date Retour</label
                    >
                    <div class="mt-1">
                      <input
                        type="date"
                        name="email"
                        id="email"
                        class="block w-full rounded-md px-3 py-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                        placeholder=""
                        v-model="myReservation.date_retour"
                      />
                    </div>
                  </div>
                </div>

                <div class="mt-4">
                  <button
                    type="button"
                    class="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                    @click="ajouterUneReservation()"
                  >
                    Book Now
                  </button>

                  <button
                    type="button"
                    class="inline-flex justify-center rounded-md border border-transparent ml-2 bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                    @click="closeModal"
                  >
                    Retour
                  </button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
</template>
<script>
import {
  TransitionChild,
  TransitionRoot,
  Dialog,
  DialogPanel,
  DialogTitle,
  Switch,
} from "@headlessui/vue";
export default {
  components: {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
    Switch,
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
        nbrPlace: 1,
        retour_inclut: false,
        date_depart: "",
        date_retour: "",
        optionChampagne: false,
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
        console.log(this.myReservation);
      this.$store.dispatch("ajoutReservation", this.myReservation);
    },
  },
  computed: {
    total() {
        let res = this.myReservation.nbrPlace * this.fly.montant 
        this.myReservation.optionChampagne ? res+=100 : null;
        this.myReservation.retour_inclut ? res*=2 :null;
        return res
    }
  },
  watch: {
    total(newValue, oldValue) {
        
    }
  },
};
</script>
<style lang=""></style>