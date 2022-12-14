<template>
  <div class="flex min-h-full">
    <div
      class="
        flex flex-1 flex-col
        justify-center
        py-6
        px-4
        sm:px-6
        lg:px-10
        xl:px-10
      "
    >
      <div class="flex min-h-full flex-col justify-center sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
          <img class="mx-auto h-auto w-max" src="/train.png" alt="Booking Vol" />
          <h2
            class="text-center text-3xl font-bold tracking-tight text-gray-900"
          >
            Où voulez-vous aller ?
          </h2>
        </div>

        <div class="mt-6 sm:mx-auto sm:w-full sm:max-w-3xl">
          <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
            <form class="space-y-6" action="#" method="POST">
              <Combobox as="div" v-model="selectedDepart">
                <ComboboxLabel class="block text-sm font-medium text-gray-700"
                  >Départ</ComboboxLabel
                >
                <div class="relative mt-1">
                  <ComboboxInput
                    class="
                      w-full
                      rounded-md
                      border border-gray-300
                      bg-white
                      py-2
                      pl-3
                      pr-10
                      shadow-sm
                      focus:border-blue-500
                      focus:outline-none
                      focus:ring-1
                      focus:ring-blue-500
                      sm:text-sm
                    "
                    @change="queryDepart = $event.target.value"
                    :display-value="(place) => place"
                  />
                  <ComboboxButton
                    class="
                      absolute
                      inset-y-0
                      right-0
                      flex
                      items-center
                      rounded-r-md
                      px-2
                      focus:outline-none
                    "
                  >
                    <ChevronUpDownIcon
                      class="h-5 w-5 text-gray-400"
                      aria-hidden="true"
                    />
                  </ComboboxButton>

                  <ComboboxOptions
                    v-if="filtedDepart.length > 0"
                    class="
                      absolute
                      z-10
                      mt-1
                      max-h-60
                      w-full
                      overflow-auto
                      rounded-md
                      bg-white
                      py-1
                      text-base
                      shadow-lg
                      ring-1 ring-black ring-opacity-5
                      focus:outline-none
                      sm:text-sm
                    "
                  >
                    <ComboboxOption
                      v-for="(place, index) in filtedDepart"
                      :key="index"
                      :value="place"
                      as="template"
                      v-slot="{ active, selected }"
                    >
                      <li
                        :class="[
                          'relative cursor-default select-none py-2 pl-8 pr-4',
                          active ? 'bg-blue-600 text-white' : 'text-gray-900',
                        ]"
                      >
                        <span
                          :class="[
                            'block truncate',
                            selected && 'font-semibold',
                          ]"
                        >
                          {{ place }}
                        </span>

                        <span
                          v-if="selected"
                          :class="[
                            'absolute inset-y-0 left-0 flex items-center pl-1.5',
                            active ? 'text-white' : 'text-blue-600',
                          ]"
                        >
                          <CheckIcon class="h-5 w-5" aria-hidden="true" />
                        </span>
                      </li>
                    </ComboboxOption>
                  </ComboboxOptions>
                </div>
              </Combobox>

              <Combobox as="div" v-model="selectedDestination">
                <ComboboxLabel class="block text-sm font-medium text-gray-700"
                  >Destination</ComboboxLabel
                >
                <div class="relative mt-1">
                  <ComboboxInput
                    class="
                      w-full
                      rounded-md
                      border border-gray-300
                      bg-white
                      py-2
                      pl-3
                      pr-10
                      shadow-sm
                      focus:border-blue-500
                      focus:outline-none
                      focus:ring-1
                      focus:ring-blue-500
                      sm:text-sm
                    "
                    @change="queryDestination = $event.target.value"
                    :display-value="(place) => place"
                  />
                  <ComboboxButton
                    class="
                      absolute
                      inset-y-0
                      right-0
                      flex
                      items-center
                      rounded-r-md
                      px-2
                      focus:outline-none
                    "
                  >
                    <ChevronUpDownIcon
                      class="h-5 w-5 text-gray-400"
                      aria-hidden="true"
                    />
                  </ComboboxButton>

                  <ComboboxOptions
                    v-if="filtedDestination.length > 0"
                    class="
                      absolute
                      z-10
                      mt-1
                      max-h-60
                      w-full
                      overflow-auto
                      rounded-md
                      bg-white
                      py-1
                      text-base
                      shadow-lg
                      ring-1 ring-black ring-opacity-5
                      focus:outline-none
                      sm:text-sm
                    "
                  >
                    <ComboboxOption
                      v-for="(place, index) in filtedDestination"
                      :key="index"
                      :value="place"
                      as="template"
                      v-slot="{ active, selected }"
                    >
                      <li
                        :class="[
                          'relative cursor-default select-none py-2 pl-8 pr-4',
                          active ? 'bg-blue-600 text-white' : 'text-gray-900',
                        ]"
                      >
                        <span
                          :class="[
                            'block truncate',
                            selected && 'font-semibold',
                          ]"
                        >
                          {{ place }}
                        </span>

                        <span
                          v-if="selected"
                          :class="[
                            'absolute inset-y-0 left-0 flex items-center pl-1.5',
                            active ? 'text-white' : 'text-blue-600',
                          ]"
                        >
                          <CheckIcon class="h-5 w-5" aria-hidden="true" />
                        </span>
                      </li>
                    </ComboboxOption>
                  </ComboboxOptions>
                </div>
              </Combobox>

              <div>
                <label
                  for="password"
                  class="block text-sm font-medium text-gray-700"
                  >Nombre de places</label
                >
                <div class="mt-1">
                  <input
                    id="password"
                    type="number"
                    v-model="nbPlaces"
                    class="
                      block
                      w-full
                      appearance-none
                      rounded-md
                      border border-gray-300
                      px-3
                      py-2
                      placeholder-gray-400
                      shadow-sm
                      focus:border-blue-500
                      focus:outline-none
                      focus:ring-blue-500
                      sm:text-sm
                    "
                  />
                </div>
              </div>

              <div class="flex justify-between">
                <button
                  type="button"
                  @click="searchVol()"
                  :class="
                    !this.selectedDepart || !this.selectedDestination
                      ? 'opacity-25 cursor-not-allowed'
                      : null
                  "
                  :disabled="!this.selectedDepart || !this.selectedDestination"
                  class="
                    flex
                    w-full
                    justify-center
                    rounded-md
                    border border-transparent
                    bg-blue-500
                    py-2
                    px-4
                    text-sm
                    font-medium
                    text-white
                    shadow-sm
                    hover:bg-blue-700
                    focus:outline-none
                    focus:ring-2
                    focus:ring-blue-500
                    focus:ring-offset-2
                    mr-3
                  "
                >
                  Chercher
                </button>
                <button
                  type="button"
                  :class="
                    !this.selectedDepart || !this.selectedDestination
                      ? 'opacity-25 cursor-not-allowed'
                      : null
                  "
                  :disabled="!this.selectedDepart || !this.selectedDestination"
                  @click="resetSearch()"
                  class="
                    flex
                    w-full
                    justify-center
                    rounded-md
                    border border-transparent
                    bg-blue-500
                    py-2
                    px-4
                    text-sm
                    font-medium
                    text-white
                    shadow-sm
                    hover:bg-blue-700
                    focus:outline-none
                    focus:ring-2
                    focus:ring-blue-500
                    focus:ring-offset-2
                  "
                >
                  Reset
                </button>
              </div>
            </form>
          </div>
          <div class="pt-5" v-for="item in trains" :key="item.id">
            <TrainItem :fly="item" />
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="relative hidden w-0 flex-1 lg:block">
      <img class="absolute inset-0 h-full w-full object-cover" src="https://images.unsplash.com/photo-1519666336592-e225a99dcd2f?&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80" alt="" />
    </div> -->
  </div>
</template>
<script>
import {
  Combobox,
  ComboboxButton,
  ComboboxInput,
  ComboboxLabel,
  ComboboxOption,
  ComboboxOptions,
  TransitionChild,
  TransitionRoot,
  Dialog,
  DialogPanel,
  DialogTitle,
  Switch,
} from "@headlessui/vue";
import { CheckIcon, ChevronUpDownIcon } from "@heroicons/vue/20/solid";
import TrainItem from "./TrainItem.vue";
import axios from "axios";
import { mapGetters, mapState } from "vuex";

export default {
  name: "HomeComponent",
  components: {
    Combobox,
    ComboboxButton,
    ComboboxInput,
    ComboboxLabel,
    ComboboxOption,
    ComboboxOptions,
    CheckIcon,
    ChevronUpDownIcon,
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
    Switch,
    TrainItem,
  },
  data() {
    return {
      queryDepart: "",
      queryDestination: "",
      enabled: false,
      isOpen: false,
      selectedDepart: null,
      selectedDestination: null,
      nbPlaces: 1,
      placesDepart: [],
      placesDestination: [],

      destination: [],
    };
  },

  methods: {
    closeModal() {
      this.isOpen = false;
    },
    openModal() {
      this.isOpen = true;
    },
    searchVol() {
      const res = this.trains.filter((vol) => {
        return (
          vol.depart == this.selectedDepart &&
          vol.arrive == this.selectedDestination &&
          vol.places >= this.nbPlaces
        );
      });
      this.$store.commit("SET_TRAIN", res);

      console.log(res);
      //console.log(this.selectedDepart);
      //console.log(this.selectedDestination);
      //console.log(this.nbPlaces);
    },
    async resetSearch() {
      this.selectedDepart = null;
      this.selectedDestination = null;
      this.$store.dispatch("fetchVols");
    },
  },
  async created() {
    const res = await this.$store.dispatch("fetchTrain");

    res.map((place) => {
      this.placesDepart.push(place.depart);
      this.placesDestination.push(place.arrive);
    });
    this.placesDepart = [...new Set(this.placesDepart)];
    this.placesDestination = [...new Set(this.placesDestination)];

    //appeler la methode addReservation pour enregistre une nouvelle reservation
  },
  computed: {
    ...mapState(["trains"]),
    filtedDepart() {
      return this.queryDepart === ""
        ? this.placesDepart
        : this.placesDepart.filter((place) => {
            return place.toLowerCase().includes(this.queryDepart.toLowerCase());
          });
    },
    filtedDestination() {
      return this.queryDestination === ""
        ? this.placesDestination
        : this.placesDestination.filter((place) => {
            return place
              .toLowerCase()
              .includes(this.queryDestination.toLowerCase());
          });
    },
  },
};
</script>
<style lang=""></style>