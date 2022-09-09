<template>
  <div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <img class="mx-auto h-28 w-auto" src="/logo.png" alt="Booking Vol" />
      <h2
        class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900"
      >
        Booking Vol
      </h2>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-3xl">
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
                  v-for="(place,index) in filtedDepart"
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
                      :class="['block truncate', selected && 'font-semibold']"
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
                  v-for="(place,index) in filtedDestination"
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
                      :class="['block truncate', selected && 'font-semibold']"
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
                  focus:border-blue-500 focus:outline-none focus:ring-blue-500
                  sm:text-sm
                "
              />
            </div>
          </div>

          <div>
            <button
              type="button"
              @click="searchVol()"
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
              Chercher
            </button>
          </div>
        </form>
      </div>
      <div class="pt-5" v-for="item in volss"  :key="item.id">
        <VolItem :fly="item" />
      </div>
    </div>
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
import VolItem from "./VolItem.vue";
import axios from "axios";
import { mapGetters } from "vuex";

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
    VolItem,
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
      volss: [],
      places: [],
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
    searchVol(){
      console.log(this.selectedDepart);
      console.log(this.selectedDestination);
      console.log(this.nbPlaces);

    }
  },
  async created() {
    this.volss = await this.$store.dispatch("fetchVols");
    this.volss.map(place => {
      this.places.push(place.depart)
    })
    this.places = [...new Set(this.places)]

  },
  computed: {
    ...mapGetters({
      vols: "getVols",
    }),
    filtedDepart() {
      return this.queryDepart === ""
        ? this.places
        : this.places.filter((place) => {
            return place
              .toLowerCase()
              .includes(this.queryDepart.toLowerCase());
          });
    },
    filtedDestination() {
      return this.queryDestination === ""
        ? this.places
        : this.places.filter((place) => {
            return place
              .toLowerCase()
              .includes(this.queryDestination.toLowerCase());
          });
    },
    
  },
};
</script>
<style lang="">
</style>