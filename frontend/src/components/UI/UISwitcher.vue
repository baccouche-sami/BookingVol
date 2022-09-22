<template>
  <div class="inline-flex rounded-md shadow-sm">
    <button
      type="button"
      class="
        relative
        inline-flex
        items-center
        rounded-l-md
        border border-gray-300
        bg-white
        px-4
        py-2
        text-sm
        font-medium
        text-gray-700
        hover:bg-gray-50
        focus:z-10
        focus:border-blue-500
        focus:outline-none
        focus:ring-1
        focus:ring-blue-500
      "
    >
      <CurrencyEuroIcon class="h-5 w-5 text-blue-500" aria-hidden="true" v-if="currency==='EURO'"  />
      <CurrencyDollarIcon  class="h-5 w-5 text-blue-500" aria-hidden="true" v-if="currency==='DOLLAR'" />

    </button>
    <Menu as="div" class="relative -ml-px block">
      <MenuButton
        class="
          relative
          inline-flex
          items-center
          rounded-r-md
          border border-gray-300
          bg-white
          px-2
          py-2
          text-sm
          font-medium
          text-gray-500
          hover:bg-gray-50
          focus:z-10
          focus:border-blue-500
          focus:outline-none
          focus:ring-1
          focus:ring-blue-500
        "
      >
        <span class="sr-only">Open options</span>
        <ChevronDownIcon class="h-5 w-5" aria-hidden="true" />
      </MenuButton>
      <transition
        enter-active-class="transition ease-out duration-100"
        enter-from-class="transform opacity-0 scale-95"
        enter-to-class="transform opacity-100 scale-100"
        leave-active-class="transition ease-in duration-75"
        leave-from-class="transform opacity-100 scale-100"
        leave-to-class="transform opacity-0 scale-95"
      >
        <MenuItems
          class="
            absolute
            right-0
            z-10
            mt-2
            -mr-1
            w-56
            origin-top-right
            rounded-md
            bg-white
            shadow-lg
            ring-1 ring-black ring-opacity-5
            focus:outline-none
          "
        >
          <div class="py-1">
            <MenuItem
              v-for="item in items"
              :key="item.name"
              v-slot="{ active }"
            >
              <a
                :href="item.href"
                :class="[
                  active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                  'block px-4 py-2 text-sm',
                ]"
                @click="switcher(item.name)"

                >{{ item.name }}</a
              >
            </MenuItem>
          </div>
        </MenuItems>
      </transition>
    </Menu>
  </div>

</template>

<script>
import { useStore } from "vuex";
import { computed } from "vue";
import {
  CurrencyDollarIcon,
  CurrencyEuroIcon,
  ChevronDownIcon,
} from "@heroicons/vue/20/solid";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
export default {
  components: {
    CurrencyDollarIcon,
    CurrencyEuroIcon,
    ChevronDownIcon,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
  },
  setup() {
    const store = useStore();
    const items = [
      { name: "EURO", href: "#", active: true },
      { name: "DOLLAR", href: "#" },
    ];
    function switcher(currency) {
      store.commit("SET_DEVIS", currency);
    }
    return {
      currency: computed(() => store.state.currency),
      switcher,
      items,
    };
  },
};
</script>