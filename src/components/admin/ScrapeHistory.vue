<template>
  <section class="section">
      <div class="subtitle">Scrape History</div>
      <b-table :data="scrapeData" :columns="columns"></b-table>
  </section>
</template>

<script>
// const _ = require('lodash/core')
import _ from 'lodash'
// import {retailer_config} from '../../lib/retailers'
// import { timeDiffToNow } from "../../lib/time"

export default {
  name: "Scrapes",
  components: {},
  props: {
    retailer: String,
  },
  data() {
    return {
      message: "Hello",
      scrapeDataResponse: [],
      scrapeData: [],
      columns: [
          // {
          //     field: '_id',
          //     label: 'ID',
          //     width: '40',
          //     numeric: false
          // },
          {
              field: 'retailer',
              label: 'Retailer',
          },
          {
              field: 'category',
              label: 'Category',
          },
          {
              field: 'success',
              label: 'Success Count',
              numeric: true
          },
          {
              field: 'failure',
              label: 'Failure Count',
              numeric: true
          },
          {
              field: 'date',
              label: 'Date',
              centered: true
          }
      ]

    }
  },
  created() {
    this.getData()
  },
  computed: {
    retailers: function () {
      return null//retailer_config
    },
    retailerData: function () {
      return this.retailers[this.retailer] || {}
    },
  },
  methods: {
    async getData() {
      const res = await fetch(`../api/scrapes`)
      console.log("Endpoint response:", res)
      this.scrapeDataResponse = res.status === 200 ? await res.json() : []
      this.scrapeData = _.map(this.scrapeDataResponse, i=>{
        i.date = new Date(i.createdAt).toLocaleString()
        return i
      })
      console.log("Data:", this.scrapeData)

      // const data = this.$papa.parse(csv, {download: true, delimiter: ",", newline: "", complete: function(results, file) {
      //   console.log("Parsing complete:", results, file)
      // }})
      // console.log(data)
      // this.unparsedResults = this.$papa.unparse(this.sampleData, {
      //   delimiter: ","
      // })
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
a {
  color: #42b983;
}
.subtitle{
  font-size: 1.8rem;
}
section.products{
    display: flex;
    flex-direction: column;
}
.scrape-output {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 0 20px;
}
</style>
